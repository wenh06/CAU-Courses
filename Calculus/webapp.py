from datetime import datetime
from pathlib import Path

import bcrypt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="2023秋微积分查询随堂测验成绩", page_icon="📜", layout="centered")


Path(__file__).parent.joinpath(".logs").mkdir(exist_ok=True)


if "dropped_columns" not in st.session_state:
    st.session_state["dropped_columns"] = []


@st.cache_resource
def load_table():
    path = "/home/wenh06/Jupyter/wenhao/resources/2023秋微积分随堂测验.xlsx"
    table = pd.read_excel(path)
    table = table.set_index("学生用户名")
    password_table = pd.read_csv("/home/wenh06/Jupyter/wenhao/resources/2023秋微积分查询密码-加密.csv")[["学生用户名", "密码"]]
    password_table["密码"] = password_table["密码"].apply(lambda p: eval(p))  # string of bytes to bytes
    table = table.join(password_table.set_index("学生用户名"))
    table = table.fillna(-1)
    # drop columns with all -1 values
    st.session_state["dropped_columns"] = [c for c in table.columns if all(table[c] == -1)]
    table = table.drop(columns=st.session_state["dropped_columns"])
    for col in table.columns:
        if col not in ["学生姓名", "密码", "所属分组", "班级"]:
            # convert from float to int
            table[col] = table[col].astype("int")
    return table


table = load_table()


st.title("2023秋微积分查询随堂测验成绩")

# name = st.text_input("姓名", help="请输入姓名", key="name")
student_id = st.text_input("学号", help="请输入学号", key="student_id")

password = st.text_input("密码", help="请输入密码", key="password", type="password")

magic_name = "郭德纲"
magic_student_id = 110
magic_password = b"$2b$12$uWlKeOBuUFoLLFSyt0qZ2.rpbjk1dbWHG/AT3qT9heTEwa4hiPgWG"


def consult():
    # if name == "" or student_id == "":
    #     st.error("姓名和学号不能为空")
    #     return
    if student_id == "":
        st.error("学号不能为空")
        return
    try:
        int(student_id)
    except ValueError:
        st.error("学号必须为数字")
        return
    if int(student_id) not in table.index and int(student_id) != magic_student_id:
        st.error("学号不存在")
        return
    # if name not in table["学生姓名"].values and name != magic_name:
    #     st.error("姓名不存在")
    #     return

    if password == "":
        st.error("密码不能为空")
        return

    # if int(student_id) == magic_student_id and name == magic_name and bcrypt.checkpw(password.encode("utf-8"), magic_password):
    #     # show the whole table
    #     st.table(table[[c for c in table.columns if c not in ["密码", "所属分组"]]])
    #     if -1 in table.values:
    #         st.write("注：-1 表示未参加随堂测验")
    #     return

    # row = table[(table.index == int(student_id)) & (table["学生姓名"] == name)]
    # if len(row) != 1:
    #     st.error("学号和姓名不匹配")
    #     return
    row = table[table.index == int(student_id)]

    # if password != row["密码"].values[0]:
    if not bcrypt.checkpw(password.encode("utf-8"), row["密码"].values[0]):
        st.error("密码错误")
        return

    # remove password column
    row = row.drop(columns=["密码", "所属分组"])
    st.table(row)
    # check if -1 in the row cells
    if -1 in row.values:
        st.write("注：-1 表示未参加随堂测验")


# add a button to call function consult

# st.button("查询", on_click=consult)

consult_button = st.button("查询", help="查询成绩")

if consult_button:
    consult()


# sidebar for admin

if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = 0

# workaround for password attempt limit
# st.session_state destroyed after refresh page (new session)
# TODO: use streamlit_authenticator instead
MAX_RETRIES = 3
if "remain_retries" not in st.session_state:
    st.session_state["remain_retries"] = MAX_RETRIES
PW_ERR_CD = 10  # seconds
if "cooldown" not in st.session_state:
    st.session_state["cooldown"] = {
        "status": 0,  # 0: not in cooldown, 1: in cooldown
        "time": datetime.now().timestamp(),
    }

st.sidebar.markdown("**管理员功能**")

if not st.session_state.is_admin:
    admin_password = st.sidebar.text_input("管理员密码", help="请输入管理员密码", key="admin_password", type="password")
    admin_login_button = st.sidebar.button("管理员登录", help="管理员登录")

    if admin_login_button:
        if st.session_state.cooldown["status"]:
            time_remaining = PW_ERR_CD - int(datetime.now().timestamp() - st.session_state.cooldown["time"])
            if time_remaining <= 0:
                st.session_state.cooldown = {
                    "status": 0,  # 0: not in cooldown, 1: in cooldown
                    "time": datetime.now().timestamp(),
                }
                st.session_state.remain_retries = MAX_RETRIES
            else:
                st.sidebar.error(f"请等待 {time_remaining} 秒后再尝试")
        else:
            if bcrypt.checkpw(admin_password.encode("utf-8"), magic_password):
                st.sidebar.success("登录成功")
                st.session_state.is_admin = 1
                st.session_state.cooldown = {
                    "status": 0,  # 0: not in cooldown, 1: in cooldown
                    "time": datetime.now().timestamp(),
                }
                st.session_state.remain_retries = MAX_RETRIES
                st.rerun()
            elif st.session_state.remain_retries > 0:
                st.sidebar.error(f"密码错误，剩余尝试次数 {st.session_state.remain_retries}")
                st.session_state.remain_retries -= 1
            else:  # st.session_state.remain_retries == 0
                st.sidebar.error(f"达到最大尝试次数，{PW_ERR_CD} 秒后再试")
                st.session_state.cooldown = {
                    "status": 1,  # 0: not in cooldown, 1: in cooldown
                    "time": datetime.now().timestamp(),
                }
                st.session_state.remain_retries = MAX_RETRIES


NON_EDITABLE_COLUMNS = ["学生姓名", "班级", "学生用户名"]
SECRET_COLUMNS = ["密码", "所属分组"]

# if bcrypt.checkpw(st.session_state["admin_password"].encode("utf-8"), magic_password):
if st.session_state.is_admin:
    # logout button
    logout_button = st.sidebar.button("管理员登出", help="管理员登出")
    if logout_button:
        st.sidebar.success("登出成功")
        # st.session_state["is_admin"] = False
        st.session_state.is_admin = False
        st.session_state.edit_table = False
        # reload the page
        st.rerun()
    else:
        # reload table button
        reload_button = st.sidebar.button("重新加载表格", help="重新加载表格")
        if reload_button:
            # clear cache
            st.cache_resource.clear()
            # reload table
            table = load_table()
            st.success("表格已重新加载")
        # show the whole table
        show_table_button = st.sidebar.button("显示所有学生成绩", help="显示所有学生成绩")
        if show_table_button:
            if st.session_state.get("edit_table", False):
                st.sidebar.error("请先退出编辑")
            else:
                st.table(table[[c for c in table.columns if c not in SECRET_COLUMNS]])
        edit_table_button = st.sidebar.button("编辑成绩", help="编辑成绩")
        save_edited_table_button = st.sidebar.button("保存编辑", help="保存编辑")
        quit_edit_button = st.sidebar.button("退出编辑", help="退出编辑")
        if "edit_table" not in st.session_state:
            st.session_state["edit_table"] = False
        if edit_table_button:
            st.session_state.edit_table = True
        if quit_edit_button:
            st.session_state.edit_table = False
        if not show_table_button and st.session_state.edit_table:
            if "edited_df" not in st.session_state:
                st.session_state["edited_df"] = table.copy()

            edited_df = st.data_editor(
                st.session_state.edited_df[[c for c in st.session_state.edited_df if c not in SECRET_COLUMNS]],
                disabled=NON_EDITABLE_COLUMNS,
                use_container_width=True,
            )

            # update st.session_state.edited_df
            for c in st.session_state.edited_df.columns:
                if c not in SECRET_COLUMNS:
                    st.session_state.edited_df[c] = edited_df[c]

        if save_edited_table_button:
            if not st.session_state.edit_table:
                st.sidebar.error("不在编辑状态")
            else:
                raw_table = pd.read_excel("/home/wenh06/Jupyter/wenhao/resources/2023秋微积分随堂测验.xlsx")
                raw_table = raw_table.set_index("学生用户名")
                for c in raw_table.columns:
                    if c in st.session_state.edited_df.columns:
                        raw_table[c] = st.session_state.edited_df[c]
                raw_table.to_excel("/home/wenh06/Jupyter/wenhao/resources/2023秋微积分随堂测验.xlsx")
                st.sidebar.success("保存成功")
                # clear cache
                st.cache_resource.clear()
                # reload table
                table = load_table()
                # st.success("表格已重新加载")

# command to run:
# nohup streamlit run webapp.py --server.port 8501 > .logs/webapp.log 2>&1 & echo $! > .logs/webapp.pid
