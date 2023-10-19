from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="2023秋微积分查询随堂测验成绩", page_icon="📜", layout="centered")


Path(__file__).parent.joinpath(".logs").mkdir(exist_ok=True)


@st.cache_resource
def load_table():
    path = "/home/wenh06/Jupyter/wenhao/resources/2023秋微积分随堂测验.xls"
    table = pd.read_excel(path)
    table = table.set_index("学生用户名")
    password_table = pd.read_csv("/home/wenh06/Jupyter/wenhao/resources/2023秋微积分查询密码.csv")[["学生用户名", "密码"]]
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
    if name == "" or student_id == "":
        st.error("姓名和学号不能为空")
        return
    try:
        int(student_id)
    except ValueError:
        st.error("学号必须为数字")
        return
    if int(student_id) not in table.index:
        st.error("学号不存在")
        return
    if name not in table["学生姓名"].values:
        st.error("姓名不存在")
        return

    row = table[(table.index == int(student_id)) & (table["学生姓名"] == name)]
    if len(row) != 1:
        st.error("学号和姓名不匹配")
        return

    if password == "":
        st.error("密码不能为空")
        return
    if password != row["密码"].values[0]:
        st.error("密码错误")
        return

    # remove password column
    row = row.drop(columns=["密码", "所属分组"])
    st.table(row)
    # check if -1 in the row cells
    if -1 in row.values:
        st.write("-1 表示未参加随堂测验")


# add a button to call function consult

st.button("查询", on_click=consult)

# command to run:
# nohup streamlit run webapp.py --server.port 8501 > .logs/webapp.log 2>&1 & echo $! > .logs/webapp.pid
