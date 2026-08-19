# Installation Guide

This guide describes a simple Windows setup for CadQuery and CQ-Editor.

## 1. Install Python With Miniconda

Download Miniconda from:

https://docs.conda.io/en/latest/miniconda.html

Recommended choice:

- Windows 64-bit installer
- Install for current user
- Do not need to add Conda to system PATH if you use the Anaconda Prompt

## 2. Create a CadQuery Environment

Open Anaconda Prompt and run:

```powershell
conda create -n cq python=3.11
conda activate cq
conda install -c conda-forge cadquery
```

Check the install:

```powershell
python -c "import cadquery as cq; print(cq.__version__)"
```

## 3. Install CQ-Editor

CQ-Editor is the recommended viewer/editor for CadQuery scripts.

Typical options:

- Download a Windows executable/release package if available.
- Or install from the CQ-Editor project instructions.

After installation, launch CQ-Editor and test:

```python
import cadquery as cq

result = cq.Workplane("XY").box(40, 20, 5)
show_object(result)
```

## 4. Optional: Install FreeCAD

FreeCAD is useful for:

- Opening STEP files from CadQuery
- Measuring imported geometry
- Exporting IGES or other exchange formats
- Running Python scripts through `freecadcmd.exe`

FreeCAD native project files use `.FCStd`; STEP exchange files use `.step` or `.stp`.

## 5. Optional: Use opencode Instead of ChatGPT

For environments where ChatGPT is not available, opencode or another coding-agent interface can be used as the automation layer.

The desired role is the same:

```text
AI coding agent
    writes/edits CadQuery scripts
    runs geometry checks
    opens the model in CQ-Editor or FreeCAD
```

## 6. Example Workflow

```powershell
conda activate cq
python examples/my_part.py
```

Then open the script in CQ-Editor and press Run.

