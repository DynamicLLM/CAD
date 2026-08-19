import cadquery as cq


# Conceptual machining setup: target part inside oversized stock.
TARGET_LENGTH = 80.0
TARGET_WIDTH = 36.0
TARGET_HEIGHT = 18.0
STOCK_ALLOWANCE = 6.0

target = (
    cq.Workplane("XY")
    .box(TARGET_LENGTH, TARGET_WIDTH, TARGET_HEIGHT)
    .edges("|Z")
    .fillet(3)
)

stock = cq.Workplane("XY").box(
    TARGET_LENGTH + 2 * STOCK_ALLOWANCE,
    TARGET_WIDTH + 2 * STOCK_ALLOWANCE,
    TARGET_HEIGHT + STOCK_ALLOWANCE,
)

vise_base = cq.Workplane("XY").box(TARGET_LENGTH + 40, TARGET_WIDTH + 50, 12).translate((0, 0, -22))

assembly = stock.union(vise_base)

cq.exporters.export(target, "01_target_part.step")
cq.exporters.export(stock, "02_stock_block.step")
cq.exporters.export(vise_base, "03_vise_base_concept.step")
cq.exporters.export(assembly, "04_machining_setup_assembly.step")

removed_volume = stock.val().Volume() - target.val().Volume()
print(f"estimated_removed_volume={removed_volume:.3f}")

for name, shape in [
    ("01 target part", target),
    ("02 stock block", stock),
    ("03 vise base concept", vise_base),
    ("04 machining setup assembly", assembly),
]:
    try:
        show_object(shape, name=name)
    except NameError:
        pass

