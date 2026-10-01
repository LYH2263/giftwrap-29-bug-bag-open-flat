"""Serialize bag open-view detail payloads: 快照回放 + 投影摘要。"""
from __future__ import annotations
from app.services.bag_open_view import bag_projection, open_bag_flat


def shape_detail(raw: dict, dims: dict | None = None) -> dict:
    # dims 只是调用兼容：详情不重算，面积以落库快照为准。
    opened = open_bag_flat(raw, dims)
    opened["projection"] = bag_projection(opened)
    return opened
