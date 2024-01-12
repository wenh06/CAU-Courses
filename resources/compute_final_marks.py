from typing import List

import numpy as np
import pandas as pd
import torch


def 算平时成绩(row: pd.Series, 取最高的几次作业成绩: int = 7) -> float:
    平时作业_cols = [c for c in row.keys().tolist() if "作业" in c]
    作业成绩 = round(torch.topk(torch.Tensor(row[平时作业_cols]), k=取最高的几次作业成绩).values.numpy().mean() * 10)
    return 作业成绩


def 算总分(row: pd.Series, 平时成绩占比: float = 0.3, 取最高的几次作业成绩: int = 7) -> float:
    期末卷面_cols = ["期末卷面成绩"]
    作业成绩 = 算平时成绩(row, 取最高的几次作业成绩)
    最终成绩 = 作业成绩 * 平时成绩占比 + row[期末卷面_cols].mean() * (1 - 平时成绩占比)
    return 最终成绩


def 是否可能需要调整(row: pd.Series, 边缘分数: List[int] = [89, 84, 81, 77, 74]) -> bool:
    return np.floor(row["最终成绩"]).astype(int).item() in 边缘分数
