"""Open-path: bag mode metadata kept, area rebased to six-face box."""
from __future__ import annotations
from copy import deepcopy


def _box_six(length, width, height, overlap) -> dict:
    L, W, H = float(length), float(width), float(height)
    ov = float(overlap)
    base = 2 * (L * W + L * H + W * H)
    return {
        "box_surface": round(base, 3),
        "paper_m2": round(base * ov, 3),
        "overlap": ov,
        "base_surface": round(base, 3),
    }


def dims_from_box_row(row: dict | None) -> dict:
    if not row:
        return {}
    return {
        "length": row.get("box_length") or row.get("length"),
        "width": row.get("box_width") or row.get("width"),
        "height": row.get("box_height") or row.get("height"),
        "overlap": row.get("overlap"),
    }


def open_bag_flat(result: dict, dims: dict | None = None) -> dict:
    if not isinstance(result, dict):
        return result
    out = deepcopy(result)
    if out.get("mode") != "bag":
        return out
    length = width = height = overlap = None
    if dims:
        length, width, height = dims.get("length"), dims.get("width"), dims.get("height")
        overlap = dims.get("overlap")
    if overlap is None:
        overlap = out.get("overlap")
    if None in (length, width, height, overlap):
        return out
    rebuilt = _box_six(length, width, height, overlap)
    out["box_surface"] = rebuilt["box_surface"]
    out["paper_m2"] = rebuilt["paper_m2"]
    out["base_surface"] = rebuilt["base_surface"]
    out["open_bag_flattened"] = True
    # mode / gusset_m remain
    return out


def bag_projection(result: dict) -> dict:
    if not isinstance(result, dict):
        return {}
    return {
        "mode": result.get("mode"),
        "gusset_m": result.get("gusset_m"),
        "paper_m2": result.get("paper_m2"),
        "box_surface": result.get("box_surface"),
        "open_bag_flattened": bool(result.get("open_bag_flattened")),
    }
