#!/usr/bin/env python3
"""webapp_bonus.py — 2026秋微积分 上课回答问题加分名单

数据文件: data/2026秋回答问题加分记录.csv (UTF-8 或 GBK 均可)
格式: 日期,学号,姓名 —— 一行 = 一次回答, 同一学生可重复出现; 日期可留空

页面下方「平时成绩测算」：联动上方查询的学号，按作业/期中占比与目标分
实时折算达到目标所需的最低期中卷面分（回答问题加分为平时成绩上的绝对加分）。

用法：
  streamlit run webapp_bonus.py --server.port 8503
"""

from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="2026秋微积分上课回答问题加分名单", page_icon="🏅", layout="centered")

Path(__file__).parent.joinpath(".logs").mkdir(exist_ok=True)

DATA_FILE = Path(__file__).parent.joinpath("data/2026秋回答问题加分记录.csv")

MEDALS = {1: "🥇 ", 2: "🥈 ", 3: "🥉 "}

# ── 平时成绩构成（按课程政策在此调整）────────────────────────────────
FULL_SCORE_OPTIONS = [30, 40]  # 平时成绩满分可选项（分）
BONUS_PER_ANSWER = 1  # 每次回答问题加的分（平时成绩尺度上的绝对加分）
HOMEWORK_RATIO = 0.7  # 作业（10 分制）折算占平时成绩的比例
MIDTERM_RATIO = 0.3  # 期中（百分制）折算占平时成绩的比例，与作业占比之和应为 1


def fmt_ts(ts: float) -> str:
    """把时间戳格式化为易读字符串"""
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def midterm_needed(full_score: int, homework: float, target: int, bonus: float) -> float:
    """求达到目标平时成绩所需的最低期中卷面分（百分制）。

    平时成绩 = 作业折算 + 期中折算 + 回答问题加分（绝对分值，直接累加）：
      作业折算 = 作业平均/10 × 满分 × HOMEWORK_RATIO   （10 分制 → 满分尺度）
      期中折算 = 期中卷面/100 × 满分 × MIDTERM_RATIO   （百分制 → 满分尺度）
    令三者之和等于 target，解出期中卷面分。
    """
    homework_pts = homework / 10 * full_score * HOMEWORK_RATIO
    return (target - bonus - homework_pts) / (full_score * MIDTERM_RATIO) * 100


@st.cache_data
def load_records(_mtime: float) -> pd.DataFrame:
    """读取加分记录，返回 [日期, 学号, 姓名] 长表。

    _mtime 为文件修改时间，文件更新则自动失效缓存。
    """
    if not DATA_FILE.exists():
        return pd.DataFrame(columns=["日期", "学号", "姓名"])
    try:
        df = pd.read_csv(DATA_FILE, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    except UnicodeDecodeError:  # Excel 另存的 GBK
        df = pd.read_csv(DATA_FILE, dtype=str, keep_default_na=False, encoding="gb18030")
    if "日期" not in df.columns:
        df["日期"] = ""
    df["学号"] = df["学号"].str.strip().str.replace(r"\.0$", "", regex=True)
    df["姓名"] = df["姓名"].str.strip()
    df["日期"] = df["日期"].str.strip()
    return df.loc[(df["学号"] != "") & (df["姓名"] != ""), ["日期", "学号", "姓名"]]


@st.cache_data
def load_leaderboard(_mtime: float) -> pd.DataFrame:
    """按学号聚合回答次数，返回 [排名, 姓名, 学号, 次数]，并列同名次。"""
    records = load_records(_mtime)
    if records.empty:
        return pd.DataFrame(columns=["排名", "姓名", "学号", "次数"])
    df = (
        records.groupby(["学号", "姓名"], sort=False)
        .size()
        .reset_index(name="次数")
        .sort_values("次数", ascending=False)
        .reset_index(drop=True)
    )
    df.insert(0, "排名", df["次数"].rank(method="min", ascending=False).astype(int))
    return df[["排名", "姓名", "学号", "次数"]]


# ── 加载数据 ─────────────────────────────────────────────────────────
records_mtime = DATA_FILE.stat().st_mtime if DATA_FILE.exists() else 0
records = load_records(records_mtime)
leaderboard = load_leaderboard(records_mtime)

# ── 页面 ─────────────────────────────────────────────────────────────
st.title("2026秋微积分 · 上课回答问题加分名单")

if records_mtime:
    st.markdown(f"> 🕗 **数据最后更新：{fmt_ts(records_mtime)}**")
st.divider()

if records.empty:
    st.info(f"暂无记录。请在 `{DATA_FILE.name}` 中逐行添加（一行 = 一次回答，允许重复），" "保存后本页自动刷新。")
    st.stop()

col1, col2, col3 = st.columns(3)
col1.metric("🧑‍🎓 参与人数", len(leaderboard))
col2.metric("🙋 加分总人次", len(records))
col3.metric("📈 人均回答次数", f"{len(records) / len(leaderboard):.1f}")

tab_board, tab_query = st.tabs(["🏅 加分榜", "🔍 个人查询"])

with tab_board:
    board = leaderboard.copy()
    board["姓名"] = board["排名"].map(MEDALS).fillna("") + board["姓名"]
    st.dataframe(
        board,
        hide_index=True,
        width="stretch",
        column_config={
            "排名": st.column_config.NumberColumn(width="small"),
            "姓名": st.column_config.TextColumn(width="small"),
            "学号": st.column_config.TextColumn(width="small"),
            "次数": st.column_config.ProgressColumn(
                width="small", min_value=0, max_value=int(leaderboard["次数"].max()), format="%d"
            ),
        },
    )

with tab_query:
    student_id = st.text_input("学号", placeholder="例如 2026310030313", help="输入学号查询自己的回答记录", key="student_id")

    if student_id:
        sid = student_id.strip()
        if not sid.isdigit():
            st.error("学号必须是数字")
        else:
            row = leaderboard.loc[leaderboard["学号"] == sid]
            if row.empty:
                st.warning("该学号暂无加分记录")
            else:
                name = row["姓名"].iloc[0]
                count = int(row["次数"].iloc[0])
                st.success(
                    f"✨ {name} 同学本学期上课回答问题 **{count}** 次，" f"可加平时成绩 **{count * BONUS_PER_ANSWER:g}** 分"
                )
                dates = records.loc[records["学号"] == sid, "日期"].tolist()
                if any(dates):
                    with st.expander("查看明细"):
                        for i, d in enumerate(dates, 1):
                            st.write(f"- 第 {i} 次：{d if d else '日期未记录'}")

# ── 平时成绩测算（复用上方「个人查询」输入的学号）────────────────────
st.divider()
st.subheader("🧮 平时成绩测算")
st.caption(
    f"作业（10 分制）按 {HOMEWORK_RATIO:.0%}、期中（百分制）按 {MIDTERM_RATIO:.0%} 折算进平时成绩；"
    f"回答问题加分为平时成绩分值上的绝对加分（每次 +{BONUS_PER_ANSWER:g} 分）。"
)

sid_calc = st.session_state.get("student_id", "").strip()
calc_hit = leaderboard.loc[leaderboard["学号"] == sid_calc] if sid_calc.isdigit() else leaderboard.iloc[0:0]
if not sid_calc.isdigit():
    bonus = None  # 未查询或学号非法 → 不测算
else:
    # 学号合法但无记录时按 0 分加分，正常测算
    bonus = (int(calc_hit["次数"].iloc[0]) if not calc_hit.empty else 0) * BONUS_PER_ANSWER

c_full, c_hw, c_target = st.columns(3)
full_score = c_full.selectbox("平时成绩满分（分）", FULL_SCORE_OPTIONS, index=0)
homework = c_hw.number_input(
    "作业平均成绩（0~10 分，自行计算）", min_value=0.0, max_value=10.0, value=0.0, step=0.1, format="%.2f"
)
target = c_target.number_input("目标平时成绩（分）", min_value=0, max_value=full_score, value=full_score, step=1)

if bonus is None:
    st.info("请先在上方「🔍 个人查询」输入学号，查得回答问题加分后再测算")
else:
    needed = midterm_needed(full_score, homework, target, bonus)
    name = calc_hit["姓名"].iloc[0] if not calc_hit.empty else ""
    who = f"{name}同学" if name else "你"
    if needed <= 0:
        st.success(f"🎉 {who}即使期中 0 分也能达到目标平时成绩（折合期中富余 {-needed:.1f} 分，已计入加分 +{bonus:g} 分）")
    elif needed > 100:
        best = homework / 10 * full_score * HOMEWORK_RATIO + full_score * MIDTERM_RATIO + bonus
        st.warning(
            f"{who}即使期中满分（100 分）也达不到目标：平时成绩最高 **{best:.1f}** 分，"
            f"还差 {target - best:.1f} 分（已计入加分 +{bonus:g} 分）"
        )
    else:
        st.success(f"🎯 {who}期中考试需要得 **{needed:.1f}** 分（百分制卷面，已计入加分 +{bonus:g} 分）")


# command to run:
# nohup streamlit run webapp_bonus.py --server.port 8503 > .logs/webapp_bonus.log 2>&1 & echo $! > .logs/webapp_bonus.pid
