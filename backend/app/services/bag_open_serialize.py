"""Serialize run detail payloads from the persisted snapshot."""
from __future__ import annotations
from app.services.bag_open_view import bag_projection, open_bag_flat


def shape_detail(raw: dict) -> dict:
    opened = open_bag_flat(raw)
    if isinstance(opened, dict):
        opened["projection"] = bag_projection(opened)
    return opened
