"""Serialize bag open-view detail payloads."""
from __future__ import annotations
from app.services.bag_open_view import bag_projection, open_bag_flat


def shape_detail(raw: dict, dims: dict | None = None) -> dict:
    opened = open_bag_flat(raw, dims)
    opened["projection"] = bag_projection(opened)
    return opened
