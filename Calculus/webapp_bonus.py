#!/usr/bin/env python3
"""webapp_bonus.py — 秋季学期微积分 上课回答问题加分名单

数据文件: data/2026秋回答问题加分记录.csv (UTF-8 或 GBK 均可)
格式: 日期,学号,姓名 —— 一行 = 一次回答, 同一学生可重复出现; 日期可留空

页面第二个 tab「平时成绩测算」：输入学号（纯数字，位数与 CSV 记录一致；
匹配不到按 +0 分），按作业/期中占比与目标分实时折算达到目标所需的最低期中卷面分
（回答问题加分为平时成绩上的绝对加分）。作业平均成绩预设 9.5 分。
「已考完期中考试」开关：开启后改为输入期中卷面分（0~100，默认空），
实时预估平时成绩总分（四舍五入取整，封顶所选满分）。

学期窗口由系统日期动态推断（每年 9 月 1 日至次年 2 月 1 日）；加分记录文件的
last modified 不在窗口内视为本学期尚无记录，不计算、不展示。

用法（经 apache2 反代到 /app/calculus-bonus/，见
/etc/apache2/conf-enabled/calculus-bonus.conf）：
  streamlit run webapp_bonus.py --server.port 8503 --server.address 127.0.0.1 \
      --server.headless true --server.baseUrlPath /app/calculus-bonus
"""

from datetime import date, datetime
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).parent.joinpath("data/2026秋回答问题加分记录.csv")


def semester_window(today: date) -> tuple[date, date, int] | None:
    """根据系统日期返回当前学期窗口 (起始 9月1日, 结束 次年2月1日, 年份标签)；不在学期内返回 None。"""
    if today >= date(today.year, 9, 1):
        return date(today.year, 9, 1), date(today.year + 1, 2, 1), today.year
    if today < date(today.year, 2, 1):
        return date(today.year - 1, 9, 1), date(today.year, 2, 1), today.year - 1
    return None


today = datetime.now().date()
semester = semester_window(today)
sem_year = semester[2] if semester else today.year

st.set_page_config(page_title=f"{sem_year}秋微积分上课回答问题加分名单", page_icon="🏅", layout="centered")

Path(__file__).parent.joinpath(".logs").mkdir(exist_ok=True)

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

# ── 学期门控：记录文件 mtime 不在当前学期窗口内 → 不计算、不展示 ──────
mtime_date = datetime.fromtimestamp(records_mtime).date() if records_mtime else None
semester_active = semester is not None and mtime_date is not None and semester[0] <= mtime_date < semester[1]

# ── 页面 ─────────────────────────────────────────────────────────────
st.title(f"{sem_year}秋微积分 · 上课回答问题加分名单")

if not semester_active:
    if semester is None:
        st.info("当前不在学期内（学期窗口为每年 9 月 1 日至次年 2 月 1 日），暂不展示。")
    else:
        last = fmt_ts(records_mtime) if records_mtime else "文件不存在"
        st.info(
            f"暂无本学期（{sem_year} 年 9 月 1 日 — {semester[1].year} 年 2 月 1 日）加分记录："
            f"记录文件最后更新于 {last}，不在本学期窗口内，暂不展示。"
        )
    st.stop()

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

tab_board, tab_calc = st.tabs(["🏅 加分榜", "🧮 平时成绩测算"])

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

with tab_calc:
    # 学号位数以 CSV 记录为准
    id_len = int(records["学号"].str.len().mode().iloc[0])
    student_id = st.text_input("学号", placeholder="2026" + "0" * (id_len - 4), help=f"纯数字，{id_len} 位")

    sid = student_id.strip()
    if student_id and (not sid.isdigit() or len(sid) != id_len):
        st.error(f"学号必须是 {id_len} 位数字")
    elif student_id:
        row = leaderboard.loc[leaderboard["学号"] == sid]
        bonus = int(row["次数"].iloc[0]) * BONUS_PER_ANSWER if not row.empty else 0
        if row.empty:
            st.caption("未匹配到该学号的加分记录，按 +0 分测算")
        else:
            st.caption(f"已匹配：{row['姓名'].iloc[0]}，本学期回答 {bonus // BONUS_PER_ANSWER} 次，加分 +{bonus:g} 分")

        midterm_done = st.toggle("已考完期中考试", value=False, help="开启后输入期中卷面分，直接预估平时成绩")

        c_full, c_hw, c_io = st.columns(3)
        full_score = c_full.selectbox("平时成绩满分（分）", FULL_SCORE_OPTIONS, index=0)
        homework = c_hw.number_input(
            "作业平均成绩（0~10 分，自行计算）", min_value=0.0, max_value=10.0, value=9.5, step=0.1, format="%.2f"
        )
        name = row["姓名"].iloc[0] if not row.empty else ""
        who = f"{name}同学" if name else "你"

        if midterm_done:
            # ── 考后模式：由期中卷面分预估平时成绩 ──
            midterm = c_io.number_input(
                "期中考试分数（0~100）", min_value=0.0, max_value=100.0, value=None, step=0.5, format="%.1f"
            )
            if midterm is None:
                st.info("输入期中考试分数后自动计算")
            else:
                total = homework / 10 * full_score * HOMEWORK_RATIO + midterm / 100 * full_score * MIDTERM_RATIO + bonus
                total = min(int(round(total, 2) + 0.5), full_score)  # 先按2位小数归整再四舍五入取整, 封顶满分
                st.success(f"🧾 {who}预估平时成绩 **{total}** 分（满分 {full_score} 分，已计入加分 +{bonus:g} 分）")
        else:
            # ── 考前模式：求达到目标平时成绩所需的最低期中卷面分 ──
            target = c_io.number_input("目标平时成绩（分）", min_value=0, max_value=full_score, value=full_score, step=1)
            needed = midterm_needed(full_score, homework, target, bonus)
            if needed <= 0:
                st.success(
                    f"🎉 {who}即使期中 0 分也能达到目标平时成绩（折合期中富余 {-needed:.1f} 分，已计入加分 +{bonus:g} 分）"
                )
            elif needed > 100:
                best = homework / 10 * full_score * HOMEWORK_RATIO + full_score * MIDTERM_RATIO + bonus
                st.warning(
                    f"{who}即使期中满分（100 分）也达不到目标：平时成绩最高 **{best:.1f}** 分，"
                    f"还差 {target - best:.1f} 分（已计入加分 +{bonus:g} 分）"
                )
            else:
                st.success(f"🎯 {who}期中考试需要得 **{needed:.1f}** 分（百分制卷面，已计入加分 +{bonus:g} 分）")


# command to run:
# nohup streamlit run webapp_bonus.py --server.port 8503 --server.address 127.0.0.1 --server.headless true --server.baseUrlPath /app/calculus-bonus > .logs/webapp_bonus.log 2>&1 & echo $! > .logs/webapp_bonus.pid
