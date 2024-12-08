from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from packaging import version

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


@st.cache_resource
def load_contest_result():
    # path = "./data/2024选课名单.csv"
    contest_result = pd.read_csv(db_file)
    contest_result["学号"] = contest_result["学号"].astype(int)
    contest_result = contest_result.set_index("学号")
    contest_result = contest_result[["10", "11"]]
    contest_result["单元测验"] = contest_result.mean(axis=1)
    contest_result = contest_result.drop(columns=["10", "11"])
    return contest_result


contest_result = load_contest_result()

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

tab_consult, tab_compute = st.tabs(["作业缺交情况查询", "期末成绩计算"])


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


def compute_final_exam_score(contest_ratio, final_exam_ratio):
    if student_id_2 == "":
        st.error("学号不能为空")
        return 0
    try:
        int(student_id_2)
    except ValueError:
        st.error("学号必须为数字")
        return 0
    if int(student_id_2) not in table.index:
        st.error("学号不存在")
        return 0

    contest_ratio /= 100
    final_exam_ratio /= 100
    contest_score = contest_result.loc[int(student_id_2), "单元测验"] * contest_ratio  # 单元测验成绩百分制
    assignment_score = table.loc[int(student_id_2)].mean() * 10 * (1 - contest_ratio)  # 作业成绩十分制
    final_exam_score = (60 - (contest_score + assignment_score) * (1 - final_exam_ratio)) / final_exam_ratio
    final_exam_score = int(np.ceil(final_exam_score * 2)) // 2  # 向上取整到0.5分

    return final_exam_score


with tab_consult:
    student_id = st.text_input("学号", help="请输入学号", key="student_id")
    consult_button = st.button("查询", help="查询成绩")

    if consult_button or student_id:
        consult()

with tab_compute:
    form_kw = dict(key="input_form")
    if version.parse(st.__version__) >= version.parse("1.29.0"):
        form_kw["border"] = False
    form = st.form(**form_kw)
    student_id_2 = form.text_input("学号", help="请输入学号", key="student_id_2")
    contest_ratio = form.selectbox("单元测验占平时成绩百分比", [30, 20], index=1)
    final_exam_ratio = form.selectbox("期末考试占总成绩百分比", [70, 60], index=1)
    compute_button = form.form_submit_button("计算及格所需要的期末卷面最低分数")

    if compute_button or student_id_2:
        final_exam_score = compute_final_exam_score(contest_ratio, final_exam_ratio)
        if final_exam_score > 0:
            st.markdown(f"及格所需要的期末卷面最低分数为**{final_exam_score}**分")

# command to run:
# nohup streamlit run webapp_2024.py --server.port 8502 > .logs/webapp_2024.log 2>&1 & echo $! > .logs/webapp_2024.pid
