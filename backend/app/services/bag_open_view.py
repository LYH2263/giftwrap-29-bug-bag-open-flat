"""Open-path view over a persisted run.

回看只读写入快照：mode=bag 的用纸档，其 paper_m2 永远是落库时的
袋宽×(袋高+底风琴褶)×2×折边值。这里禁止拿盒子的现行边长重算
六面面积——盒边后来被改过也与旧档无关，重算只会让详情与列表不一致。
"""
from __future__ import annotations
from copy import deepcopy


def open_bag_flat(result: dict, dims: dict | None = None) -> dict:
    """返回写入快照的拷贝。

    dims 仅为兼容旧调用方保留，绝不参与面积计算：快照是唯一真相。
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
        "bag_surface": result.get("bag_surface"),
    }
