"""
由平时成绩 (作业成绩、期中成绩等) 和期末卷面成绩计算最终成绩，并输出最终成绩单。

Requirements:
    - pandas
    - numpy

Usage:

    ```bash
    python compute_final_marks.py <data_folder> [平时成绩占比 (default: 0.3)] [取最高的几次作业成绩 (optional)]
    ```

    - `data_folder`: 数据文件夹路径
    - `平时成绩占比`: 平时成绩占最终成绩的比例，默认为0.3
    - `取最高的几次作业成绩`: 取最高的几次作业成绩，默认为None，即取所有作业成绩的平均值

"""

import inspect
import sys
import warnings
from functools import partial, reduce
from pathlib import Path
from typing import List, Optional, Tuple, Union

import numpy as np
import pandas as pd


def select_k(
    arr: np.ndarray, k: Union[int, List[int], np.ndarray], dim: int = -1, largest: bool = True, sorted: bool = True
) -> Tuple[np.ndarray, np.ndarray]:
    """Select elements from an array along a specified axis of specific rankings.

    Parameters
    ----------
    arr : array_like
        Input array.
    k : int or array_like
        Number of elements to retrieve. If k is a 1D array, it represents the specific rankings to retrieve.
        NOTE that the rankings are 0-based, for example the rankings of the top 3 elements are [0, 1, 2].
    dim : int, default -1
        Axis along which to operate. Default is -1 (the last axis).
    largest : bool, default True
        If True, find the largest elements, else find the smallest elements.
    sorted : bool, default True
        If True, the result is sorted. If False, the result is not sorted.

    Returns
    -------
    values : numpy.ndarray
        The selected values along each axis.
    indices : numpy.ndarray
        The indices of the selected values along each axis.

    .. note::

        For integer k, this function has the same functionality as :func:`torch.topk`.

    """
    arr = np.asarray(arr).copy()  # copy to avoid modifying the input array
    if isinstance(k, (list, np.ndarray)):
        k = np.asarray(k)
    else:
        k = np.arange(k)
    assert -arr.ndim <= dim < arr.ndim, "dim out of bounds"
    dim = dim % arr.ndim  # convert negative dim to positive
    assert k.ndim == 1, f"k must be 1-dimensional, but got {k.ndim} dimensions"
    assert len(np.unique(k)) == len(k), "k must be unique"
    assert len(k) > 0, "k must be a non-empty array, or a positive integer"
    assert 0 <= k.min() <= k.max() <= arr.shape[dim], "k out of bounds"

    if largest:
        arr = -arr
    if sorted:
        indices = np.take(np.argsort(arr, axis=dim), k, axis=dim)
    else:
        indices = np.take(np.argpartition(arr, kth=k, axis=dim), k, axis=dim)
    values = np.take_along_axis(arr, indices, axis=dim)

    if largest:
        values = -values

    return values, indices


def np_topk(arr: np.ndarray, k: int, dim: int = -1, largest: bool = True, sorted: bool = True) -> Tuple[np.ndarray, np.ndarray]:
    """Find the k largest elements of an array along a specified axis.

    Parameters
    ----------
    arr : array_like
        Input array.
    k : int
        Number of elements to retrieve.
    dim : int, default -1
        Axis along which to operate. Default is -1 (the last axis).
    largest : bool, default True
        If True, find the largest elements, else find the smallest elements.
    sorted : bool, default True
        If True, the result is sorted. If False, the result is not sorted.

    Returns
    -------
    values : numpy.ndarray
        The k largest values along each axis.
    indices : numpy.ndarray
        The indices of the k largest values along each axis.

    .. note::

        This function has the same functionality as :func:`torch.topk`,
        but is implemented using only numpy.

    """
    # arr = np.asarray(arr).copy()  # copy to avoid modifying the input array
    # assert -arr.ndim <= dim < arr.ndim, "dim out of bounds"
    # dim = dim % arr.ndim  # convert negative dim to positive
    # assert 0 < k <= arr.shape[dim], "k out of bounds"

    # if largest:
    #     arr = -arr
    # if sorted:
    #     indices = np.take(np.argsort(arr, axis=dim), np.arange(k), axis=dim)
    # else:
    #     indices = np.take(np.argpartition(arr, kth=k, axis=dim), np.arange(k), axis=dim)
    # values = np.take_along_axis(arr, indices, axis=dim)

    # if largest:
    #     values = -values

    # return values, indices
    assert isinstance(k, int) and k > 0, "k must be a positive integer"
    return select_k(arr, k, dim, largest, sorted)


def 计算平时成绩(row: pd.Series, 取最高的几次作业成绩: Optional[int] = None) -> float:
    平时作业_cols = [c for c in row.keys().tolist() if "作业" in c]
    if 取最高的几次作业成绩 is None:
        取最高的几次作业成绩 = len(平时作业_cols)
    if 取最高的几次作业成绩 == 0:
        raise ValueError("取最高的几次作业成绩不能为0")
    if 取最高的几次作业成绩 > len(平时作业_cols):
        warnings.warn("取最高的几次作业成绩大于总作业次数，将取所有作业成绩的平均值。")
        取最高的几次作业成绩 = len(平时作业_cols)
    # 作业成绩 = round(torch.topk(torch.Tensor(row[平时作业_cols]), k=取最高的几次作业成绩).values.numpy().mean() * 10)
    作业成绩 = round(np_topk(row[平时作业_cols].to_numpy(), k=取最高的几次作业成绩)[0].mean() * 10)
    return 作业成绩


def 计算总分(row: pd.Series, 平时成绩占比: float = 0.3, 取最高的几次作业成绩: Optional[int] = None) -> float:
    assert 0 <= 平时成绩占比 <= 1, "平时成绩占比必须在0到1之间"
    期末卷面_cols = ["期末卷面成绩"]
    作业成绩 = 计算平时成绩(row, 取最高的几次作业成绩)
    最终成绩 = 作业成绩 * 平时成绩占比 + row[期末卷面_cols].mean() * (1 - 平时成绩占比)
    return 最终成绩


def 是否可能需要调整(row: pd.Series, 边缘分数: List[int] = [89, 84, 81, 77, 74]) -> bool:
    return np.floor(row["最终成绩"]).astype(int).item() in 边缘分数


if __name__ == "__main__":
    assert len(sys.argv) >= 2, "请提供数据文件夹路径"
    if sys.argv[1] in ["-h", "--help"]:
        print(
            "Usage: python compute_final_marks.py <data_folder> [平时成绩占比 (default: 0.3)] [取最高的几次作业成绩 (optional)]"
        )
        exit(0)
    data_folder = Path(sys.argv[1]).expanduser().resolve()
    if len(sys.argv) >= 3:
        平时成绩占比 = float(sys.argv[2])
    else:
        平时成绩占比 = inspect.signature(计算总分).parameters["平时成绩占比"].default
    if len(sys.argv) >= 4:
        取最高的几次作业成绩 = int(sys.argv[3])
    else:
        取最高的几次作业成绩 = inspect.signature(计算平时成绩).parameters["取最高的几次作业成绩"].default
    try:
        期末卷面成绩 = pd.read_csv(data_folder.glob("*期末卷面*.csv").__next__())
        平时作业成绩 = pd.read_csv(data_folder.glob("*作业*.csv").__next__())
        人员名单 = pd.read_csv(data_folder.glob("*人员名单*.csv").__next__())
        prefix = data_folder.glob("*期末卷面*.csv").__next__().name.split("期末卷面")[0]
    except StopIteration:
        raise FileNotFoundError(
            "请检查数据文件夹路径是否正确。" "数据文件夹应包含期末卷面成绩、平时作业成绩、人员名单三个CSV文件。"
        )
    for df in [期末卷面成绩, 平时作业成绩]:
        if "班级" in df.columns:
            df.drop(columns=["班级"], inplace=True)
    算分表格 = reduce(
        lambda left, right: pd.merge(left, right, on=["学号", "姓名"], how="outer"), [人员名单, 期末卷面成绩, 平时作业成绩]
    )
    算分表格["平时成绩"] = 算分表格.apply(partial(计算平时成绩, 取最高的几次作业成绩=取最高的几次作业成绩), axis=1)
    算分表格["最终成绩"] = 算分表格.apply(
        partial(计算总分, 平时成绩占比=平时成绩占比, 取最高的几次作业成绩=取最高的几次作业成绩), axis=1
    )
    可能需要调整名单 = 算分表格[算分表格.apply(是否可能需要调整, axis=1)]
    不及格名单 = 算分表格[算分表格["最终成绩"] < 60]
    优秀名单 = 算分表格[算分表格["最终成绩"] >= 90]

    算分表格.to_csv(data_folder / f"{prefix}最终成绩单.csv", index=False)

    print(f"优秀人数：{len(优秀名单)}, 优秀率：{len(优秀名单) / len(算分表格):.2%}")
    print(f"不及格人数：{len(不及格名单)}, 不及格率：{len(不及格名单) / len(算分表格):.2%}")

    if len(优秀名单) > 0:
        print("优秀名单：")
        print(优秀名单[["学号", "姓名", "平时成绩", "最终成绩"]])

    if len(不及格名单) > 0:
        print("不及格名单：")
        print(不及格名单[["学号", "姓名", "平时成绩", "最终成绩"]])

    if len(可能需要调整名单) > 0:
        print("可能需要调整的名单：")
        print(可能需要调整名单[["学号", "姓名", "平时成绩", "最终成绩"]])
