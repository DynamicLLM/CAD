---
name: progressive-die-flat-blanking
description: Create conceptual progressive-die geometry for flat sheet-metal blanking and piercing cases using CadQuery and CQ-Editor.
---

# Progressive Die Flat Blanking

Use this skill when the target part is mostly flat sheet metal and the main operations are piercing, trimming, and final blanking.

## Typical Case

```text
flat target STEP
        ↓
raw strip
        ↓
pilot holes
        ↓
internal piercing
        ↓
outer blanking
        ↓
final flat product
```

## Required Inputs

- target STEP or flat 2D profile
- material and sheet thickness
- punch/die clearance per side
- strip width
- station pitch
- feed direction
- minimum scrap bridge
- minimum edge web
- hole/cutout sequence if known

## CadQuery Outputs

- `01_target_product.step`
- `02_raw_strip.step`
- `03_strip_layout.step`
- `04_lower_die_openings.step`
- `05_upper_punches.step`
- `06_progressive_die_assembly.step`

## Workflow

1. Import target STEP and identify the main flat solid.
2. Measure thickness, length, width, area, and hole/cutout profiles.
3. Choose feed direction and station pitch.
4. Create raw strip with side web and scrap bridge assumptions.
5. Create early pilot holes for strip registration.
6. Create internal piercing punches before final blanking.
7. Create lower die openings with documented clearance.
8. Create final blanking punch from the outer profile.
9. Create an exploded CQ-Editor assembly so each object is visible.
10. Export and verify all STEP files.

## Validation Checks

- target product dimensions unchanged
- strip covers the part at every station
- pierce punches align with lower die openings
- clearance is positive
- final blanking happens after internal piercing
- material utilization estimate is reported
- approximate cutting force is reported if shear strength is available

