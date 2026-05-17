# Amazon Q Rules — Scratch Creator

This project enables AI agents to programmatically create and modify MIT Scratch 3.0 projects (`.sb3` files).

## Overview

Scratch `.sb3` files are ZIP archives containing `project.json` + media assets (SVG/PNG, WAV/MP3). This project provides:
- **`references/`** — 17 Markdown files with complete block opcode documentation (194+ blocks) and JSON examples
- **`scripts/`** — Python 3.7+ modules (zero external deps) for building, packing, validating .sb3 files
- **`templates/`** — 10 project templates covering common Scratch project types
- **`SKILL.md`** — Primary skill definition with detailed workflow

## How to Create Scratch Projects

### Step 1: Analyze requirements
Determine project type, sprites needed, extensions (pen, music, micro:bit, etc.).

### Step 2: Read reference docs
- `references/project-json-schema.md` for the overall structure
- Corresponding `references/blocks-*.md` files for the block opcodes you need

### Step 3: Generate the project
Use the Python scripts to build and pack:

```python
import sys; sys.path.insert(0, 'scripts')
from project_builder import ScratchProject
from block_builder import num, string

proj = ScratchProject()
proj.create_stage()
sprite = proj.create_sprite("Sprite1")
proj.add_blocks_from_chain(sprite, [
    ("event_whenflagclicked", {}, {}),
    ("motion_movesteps", {"STEPS": num(10)}, {}),
    ("looks_say", {"MESSAGE": string("Hello!")}, {}),
])
proj.save_json("output/project.json")
```

### Step 4: Pack and validate
```python
from scratch_utils import create_project_directory, pack_sb3, validate_project
create_project_directory(proj.to_dict(), 'output_dir')
pack_sb3('output_dir', 'output.sb3')
```

## Block Reference Index

| Category | Count | File |
|----------|-------|------|
| Events | 10 | `references/blocks-events.md` |
| Motion | 18 | `references/blocks-motion.md` |
| Looks | 24 | `references/blocks-looks.md` |
| Sound | 12 | `references/blocks-sound.md` |
| Control | 17 | `references/blocks-control.md` |
| Sensing | 20 | `references/blocks-sensing.md` |
| Operators | 18 | `references/blocks-operators.md` |
| Variables | 17 | `references/blocks-variables.md` |
| Music ext | 7 | `references/blocks-music.md` |
| Pen ext | 11 | `references/blocks-pen.md` |
| Video ext | 3 | `references/blocks-video.md` |
| Translate ext | 2 | `references/blocks-translate.md` |
| TTS ext | 3 | `references/blocks-texttospeech.md` |
| micro:bit | 16 | `references/blocks-microbit.md` |
| LEGO | 12+ | `references/blocks-lego.md` |
| Custom | 4 | `references/blocks-custom.md` |
| Schema | — | `references/project-json-schema.md` |

## Block JSON Format

```json
{
  "opcode": "motion_movesteps",
  "next": null, "parent": null,
  "inputs": {"STEPS": [1, [4, "10"]]},
  "fields": {},
  "shadow": false, "topLevel": true,
  "x": 0, "y": 0
}
```

**Input types:**
| Format | Meaning |
|--------|---------|
| `[1, [4, "10"]]` | Number literal |
| `[1, [10, "text"]]` | String literal |
| `[1, [12, "varId", "name"]]` | Variable reference |
| `[2, "blockId"]` | Nested reporter |
| `[3, "blockId", [10, "default"]]` | Reporter with default |

## Coordinate System
- Stage: 480 × 360 px
- x: [-240, 240], y: [-180, 180]
- Center: (0, 0)
- Direction: 0° = up, 90° = right

## Python Modules Quick Ref

**scratch_utils.py**: `unpack_sb3()`, `pack_sb3()`, `create_empty_project()`, `add_sprite()`, `create_block()`, `validate_project()`, `create_project_directory()`

**block_builder.py**: 60+ `make_*()` functions — `make_event_whenflagclicked()`, `make_movesteps(n)`, `make_say(msg)`, `make_forever()`, `make_if()`, `make_wait(s)`, `make_broadcast(name)`, etc. Input helpers: `num()`, `string()`, `variable_ref()`.

**project_builder.py**: `ScratchProject` class — `create_stage()`, `create_sprite()`, `add_variable()`, `add_blocks_from_chain()`, `add_extension()`, `save_json()`, `validate()`.

## Constraints
- .sb3 = ZIP; `project.json` at archive root
- Each sprite ≥ 1 costume; Stage ≥ 1 backdrop
- Extensions must be in project.json `extensions` array
- 50 MB limit (Scratch online)
- Python 3.7+, zero external dependencies
