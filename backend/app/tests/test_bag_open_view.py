"""回看开放视图：只读快照，任何传入的现行盒边都不得改写面积。"""
from app.services.bag_open_view import open_bag_flat, bag_projection
from app.services.bag_open_serialize import shape_detail


BAG_SNAPSHOT = {
    "mode": "bag",
    "bag_width": 0.30,
    "bag_height": 0.20,
    "gusset_m": 0.10,
    "bag_surface": 0.18,
    "overlap": 1.15,
    "paper_m2": 0.207,
    "ribbon": {"wrap_style": "cross", "ribbon_m": 1.5},
}

CURRENT_DIMS = {"length": 0.99, "width": 0.88, "height": 0.77, "overlap": 1.3}


def test_open_bag_flat_keeps_written_area_even_with_dims():
    out = open_bag_flat(BAG_SNAPSHOT, CURRENT_DIMS)
    assert out["mode"] == "bag"
    assert out["gusset_m"] == 0.10
    assert out["paper_m2"] == BAG_SNAPSHOT["paper_m2"]
    assert out.get("open_bag_flattened") is not True
    assert "box_surface" not in out
    assert "base_surface" not in out
    # 不就地改原快照
    assert BAG_SNAPSHOT["paper_m2"] == 0.207


def test_shape_detail_projection_mirrors_snapshot():
    out = shape_detail(BAG_SNAPSHOT)
    assert out["projection"] == {
        "mode": "bag",
        "gusset_m": 0.10,
        "paper_m2": 0.207,
        "box_surface": None,
        "bag_surface": 0.18,
    }


def test_open_bag_flat_box_mode_untouched():
    box = {"mode": "box", "gusset_m": None, "box_surface": 0.27, "paper_m2": 0.3105}
    out = open_bag_flat(box, CURRENT_DIMS)
    assert out == box
