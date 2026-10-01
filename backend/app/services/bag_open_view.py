"""Open-path: 详情只回放落库快照，面积禁止用现行盒边重算。

袋装两片＋底风琴褶与盒装六面是两套独立口径，写入时已定值；
回看（列表/详情）一律以写入快照为唯一真相，盒档事后被改也不影响旧档。
"""
from __future__ import annotations
from copy import deepcopy


def open_bag_flat(result: dict, dims: dict | None = None) -> dict:
    """原样回放写入快照。

    dims 仅为兼容旧调用保留，函数体不得读取：
    详情面积禁止用现行盒边重算，mode / gusset_m / paper_m2 都是落库值。
    """
    if not isinstance(result, dict):
        return result
    return deepcopy(result)


def bag_projection(result: dict) -> dict:
    if not isinstance(result, dict):
        return {}
    return {
        "mode": result.get("mode"),
        "gusset_m": result.get("gusset_m"),
        "paper_m2": result.get("paper_m2"),
        "box_surface": result.get("box_surface"),
    }
