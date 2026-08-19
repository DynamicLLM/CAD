# Progressive Die Workflow

This workflow is inspired by publicly described NX progressive die processes, rewritten as a simple open CadQuery/CQ-Editor workflow.

## Public NX Workflow Themes

Public Siemens/NX material repeatedly describes progressive die work as an associative workflow from sheet-metal part preparation through strip layout, die base assembly, inserts, validation, and drawings. The public course outlines also separate the process into staged part preparation, blank generation, blank layout, scrap design, strip layout, die base management, standard parts, piercing/forming insert design, finishing details, validation, and drawings.

In this open workflow, treat those as process stages rather than as exact NX commands.

## 1. Part Preparation

Start from a target part. If the target part is already a STEP file, import it and measure it. If it is a simple geometry, define it directly in CadQuery.

Typical checks:

- thickness
- bounding box
- holes and cutouts
- bend/form regions
- likely feed direction

## 2. Blank and Strip Planning

Create a raw strip around the target blank.

Typical parameters:

- strip width
- station pitch
- side scrap allowance
- front/back scrap bridge
- pilot hole positions
- material utilization

Material utilization can be estimated as:

```text
utilization = parts_per_pitch * part_area / (station_pitch * strip_width)
```

## 3. Station Sequence

Define stations in feed order.

Common operations:

- pilot piercing
- internal piercing
- trimming
- forming
- restrike/calibration
- final blanking/cutoff

For simple flat parts, internal holes usually happen before final blanking.

## 4. Punch and Die Geometry

Generate upper punch geometry from the cut profiles. Generate lower die openings with clearance.

For a concept model:

- upper punch can be a simplified extrusion of the cut profile
- lower die can be a block with an opening
- punch/die clearance can be represented by offset profiles where reliable

For a flat blanking concept:

```text
upper punch profile ~= target cut profile
lower die opening ~= target cut profile plus clearance
raw strip ~= rectangular or nested stock around the target profile
```

## 5. Assembly

Create a display assembly:

- target product
- raw strip
- lower die block
- upper punch bodies
- upper plate
- optional guide pins or simple reference columns

Use vertical spacing so the user can see every component in CQ-Editor.

## 6. Validation

Minimum checks:

- all STEP files exist
- re-imported STEP objects are valid
- bounding boxes are plausible
- target part dimensions are unchanged
- punches align with corresponding die openings
- raw strip covers target profiles

Advanced checks can include:

- approximate blanking force
- material utilization
- collision/interference
- center of pressure
- station balancing

## 7. Report

Every generated concept should include a short report with:

- source STEP name
- assumptions
- material values used
- station sequence
- exported STEP files
- verification results
- limitations and next engineering decisions
