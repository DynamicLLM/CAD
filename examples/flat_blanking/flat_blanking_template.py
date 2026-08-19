import cadquery as cq


# Dimensions are in millimeters. Values are conceptual placeholders.
MATERIAL = "mild steel"
SHEET_THICKNESS = 2.0
PART_LENGTH = 80.0
PART_WIDTH = 36.0
CORNER_RADIUS = 4.0
HOLE_DIAMETER = 8.0
HOLE_X_OFFSET = 24.0

PUNCH_DIE_CLEARANCE_PER_SIDE = 0.08
STRIP_WIDTH = 52.0
STATION_PITCH = 95.0
STATION_COUNT = 4
STRIP_LENGTH = STATION_PITCH * STATION_COUNT

LOWER_DIE_THICKNESS = 18.0
PUNCH_HEIGHT = 35.0
DISPLAY_GAP = 18.0


hole_points = [(-HOLE_X_OFFSET, 0), (HOLE_X_OFFSET, 0)]


def rounded_plate(length, width, radius, thickness):
    return cq.Workplane("XY").box(length, width, thickness).edges("|Z").fillet(radius)


target_part = rounded_plate(PART_LENGTH, PART_WIDTH, CORNER_RADIUS, SHEET_THICKNESS)
target_part = target_part.faces(">Z").workplane().pushPoints(hole_points).hole(HOLE_DIAMETER)

raw_strip = (
    cq.Workplane("XY")
    .box(STRIP_LENGTH, STRIP_WIDTH, SHEET_THICKNESS)
    .translate((0, -80, 0))
)

lower_die = (
    cq.Workplane("XY")
    .box(PART_LENGTH + 40, PART_WIDTH + 40, LOWER_DIE_THICKNESS)
    .translate((0, 0, -LOWER_DIE_THICKNESS / 2 - DISPLAY_GAP))
)

pierce_punches = (
    cq.Workplane("XY")
    .pushPoints(hole_points)
    .circle(HOLE_DIAMETER / 2)
    .extrude(PUNCH_HEIGHT)
    .translate((0, 0, SHEET_THICKNESS + DISPLAY_GAP))
)

blanking_punch = rounded_plate(PART_LENGTH, PART_WIDTH, CORNER_RADIUS, PUNCH_HEIGHT).translate(
    (0, 0, SHEET_THICKNESS + DISPLAY_GAP + PUNCH_HEIGHT + 5)
)

assembly = target_part.union(raw_strip).union(lower_die).union(pierce_punches).union(blanking_punch)

exports = {
    "01_target_product.step": target_part,
    "02_raw_strip.step": raw_strip,
    "03_lower_die_concept.step": lower_die,
    "04_pierce_punches.step": pierce_punches,
    "05_blanking_punch.step": blanking_punch,
    "06_flat_blanking_assembly.step": assembly,
}

for filename, shape in exports.items():
    cq.exporters.export(shape, filename)

for name, shape in [
    ("01 target product", target_part),
    ("02 raw strip", raw_strip),
    ("03 lower die concept", lower_die),
    ("04 pierce punches", pierce_punches),
    ("05 blanking punch", blanking_punch),
    ("06 assembly", assembly),
]:
    try:
        show_object(shape, name=name)
    except NameError:
        pass
