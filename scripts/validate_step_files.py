import argparse
import glob
from pathlib import Path

import cadquery as cq


def inspect_step(path: Path) -> dict:
    obj = cq.importers.importStep(str(path))
    shape = obj.val()
    bb = shape.BoundingBox()
    return {
        "file": str(path),
        "bbox_x": bb.xlen,
        "bbox_y": bb.ylen,
        "bbox_z": bb.zlen,
        "volume": shape.Volume(),
        "area": shape.Area(),
        "valid": shape.isValid(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate STEP files exported by CadQuery examples.")
    parser.add_argument("paths", nargs="+", help="STEP files to inspect")
    args = parser.parse_args()

    expanded = []
    for raw in args.paths:
        matches = glob.glob(raw)
        expanded.extend(matches if matches else [raw])

    for raw in expanded:
        path = Path(raw)
        if not path.exists():
            print(f"{path}: missing")
            continue
        try:
            info = inspect_step(path)
        except Exception as exc:
            print(f"{path}: import failed: {exc}")
            continue
        print(
            f"{info['file']}: "
            f"bbox={info['bbox_x']:.3f} x {info['bbox_y']:.3f} x {info['bbox_z']:.3f}, "
            f"volume={info['volume']:.3f}, area={info['area']:.3f}, valid={info['valid']}"
        )


if __name__ == "__main__":
    main()
