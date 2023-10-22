from pathlib import Path

import bcrypt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="2023秋微积分查询随堂测验成绩", page_icon="📜", layout="centered")


Path(__file__).parent.joinpath(".logs").mkdir(exist_ok=True)


@st.cache_resource
def load_table():
    path = "/home/wenh06/Jupyter/wenhao/resources/2023秋微积分随堂测验.xls"
    table = pd.read_excel(path)
    table = table.set_index("学生用户名")
    password_table = pd.read_csv("/home/wenh06/Jupyter/wenhao/resources/2023秋微积分查询密码-加密.csv")[["学生用户名", "密码"]]
    password_table["密码"] = password_table["密码"].apply(lambda p: eval(p))  # string of bytes to bytes
    table = table.join(password_table.set_index("学生用户名"))
    table = table.fillna(-1)
    for col in table.columns:
        if col not in ["学生姓名", "密码", "所属分组", "班级"]:
            # convert from float to int
            table[col] = table[col].astype("int")
    return table


table = load_table()

name = st.text_input("姓名", help="请输入姓名", key="name")
student_id = st.text_input("学号", help="请输入学号", key="student_id")

password = st.text_input("密码", help="请输入密码", key="password", type="password")


def consult():
    magic_name = "郭德纲"
    magic_student_id = 110
    magic_password = b"$2b$12$uWlKeOBuUFoLLFSyt0qZ2.rpbjk1dbWHG/AT3qT9heTEwa4hiPgWG"
    if name == "" or student_id == "":
        st.error("姓名和学号不能为空")
        return
    try:
        int(student_id)
    except ValueError:
        st.error("学号必须为数字")
        return
    if int(student_id) not in table.index and int(student_id) != magic_student_id:
        st.error("学号不存在")
        return
    if name not in table["学生姓名"].values and name != magic_name:
        st.error("姓名不存在")
        return

    if password == "":
        st.error("密码不能为空")
        return

    if int(student_id) == magic_student_id and name == magic_name and bcrypt.checkpw(password.encode("utf-8"), magic_password):
        # show the whole table
        st.table(table[[c for c in table.columns if c not in ["密码", "所属分组"]]])
        if -1 in table.values:
            st.write("注：-1 表示未参加随堂测验")
        return

    row = table[(table.index == int(student_id)) & (table["学生姓名"] == name)]
    if len(row) != 1:
        st.error("学号和姓名不匹配")
        return

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

st.button("查询", on_click=consult)

# command to run:
# nohup streamlit run webapp.py --server.port 8501 > .logs/webapp.log 2>&1 & echo $! > .logs/webapp.pid
