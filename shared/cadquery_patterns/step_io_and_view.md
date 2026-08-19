# CadQuery STEP IO And CQ-Editor Pattern

Use this pattern in examples and generated scripts.

```python
import cadquery as cq

result = cq.Workplane("XY").box(80, 40, 5)

cq.exporters.export(result, "01_result.step")

try:
    show_object(result, name="01 result")
except NameError:
    pass
```

## Re-Import Check

```python
obj = cq.importers.importStep("01_result.step")
bb = obj.val().BoundingBox()
print(bb.xlen, bb.ylen, bb.zlen, obj.val().Volume())
```

