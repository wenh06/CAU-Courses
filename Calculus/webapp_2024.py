from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="2024秋微积分作业缺交情况查询", page_icon="📜", layout="centered")


Path(__file__).parent.joinpath(".logs").mkdir(exist_ok=True)

db_file = Path(__file__).parent.joinpath("data/2024选课名单.csv")


@st.cache_resource
def load_table():
    # path = "./data/2024选课名单.csv"
    table = pd.read_csv(db_file)
    table["学号"] = table["学号"].astype(int)
    table = table.set_index("学号")
    table = table[list(map(str, range(1, 10)))]
    return table


table = load_table()


if "db_last_update_time" not in st.session_state:
    # set the last update time to the last modified time of the database file
    st.session_state["db_last_update_time"] = db_file.stat().st_mtime
elif db_file.stat().st_mtime > st.session_state["db_last_update_time"]:
    # clear the cache if the database file has been modified
    st.cache_resource.clear()
    # reload the table if the database file has been modified
    table = load_table()
    st.session_state["db_last_update_time"] = db_file.stat().st_mtime


st.title("2024秋微积分作业缺交情况查询")

student_id = st.text_input("学号", help="请输入学号", key="student_id")


def consult():
    if student_id == "":
        st.error("学号不能为空")
        return
    try:
        int(student_id)
    except ValueError:
        st.error("学号必须为数字")
        return
    if int(student_id) not in table.index:
        st.error("学号不存在")
        return
    row = table[table.index == int(student_id)].iloc[0].values
    indices = np.where(row == 0)[0]
    if len(indices) == 0:
        st.write("作业全部交齐")
    else:
        st.write(f"缺交第{', '.join(map(str, indices + 1))}次作业")


consult_button = st.button("查询", help="查询成绩")

if consult_button or student_id:
    consult()

# command to run:
# nohup streamlit run webapp_2024.py --server.port 8502 > .logs/webapp_2024.log 2>&1 & echo $! > .logs/webapp_2024.pid
