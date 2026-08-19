import cadquery as cq


# Conceptual fixture for a simple target block.
TARGET_LENGTH = 80.0
TARGET_WIDTH = 36.0
TARGET_HEIGHT = 12.0

BASE_LENGTH = 140.0
BASE_WIDTH = 90.0
BASE_THICKNESS = 12.0
LOCATOR_HEIGHT = 16.0
CLAMP_HEIGHT = 10.0

target = cq.Workplane("XY").box(TARGET_LENGTH, TARGET_WIDTH, TARGET_HEIGHT).translate((0, 0, BASE_THICKNESS + TARGET_HEIGHT / 2))
base = cq.Workplane("XY").box(BASE_LENGTH, BASE_WIDTH, BASE_THICKNESS)

locators = (
    cq.Workplane("XY")
    .pushPoints([(-45, -28), (45, -28), (-45, 28)])
    .box(10, 10, LOCATOR_HEIGHT)
    .translate((0, 0, BASE_THICKNESS / 2 + LOCATOR_HEIGHT / 2))
)

clamps = (
    cq.Workplane("XY")
    .pushPoints([(0, 32), (0, -32)])
    .box(36, 8, CLAMP_HEIGHT)
    .translate((0, 0, BASE_THICKNESS + TARGET_HEIGHT + CLAMP_HEIGHT / 2))
)

assembly = base.union(target).union(locators).union(clamps)

cq.exporters.export(target, "01_target_reference.step")
cq.exporters.export(base, "02_fixture_base.step")
cq.exporters.export(locators, "03_locators.step")
cq.exporters.export(clamps, "04_clamps.step")
cq.exporters.export(assembly, "05_fixture_assembly.step")

for name, shape in [
    ("01 target reference", target),
    ("02 fixture base", base),
    ("03 locators", locators),
    ("04 clamps", clamps),
    ("05 fixture assembly", assembly),
]:
    try:
        show_object(shape, name=name)
    except NameError:
        pass

