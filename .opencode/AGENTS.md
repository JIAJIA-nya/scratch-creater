# AGENTS.md — Scratch Creator

Scratch Creator enables AI agents to create and modify MIT Scratch 3.0 projects (`.sb3` files) programmatically. The `.sb3` format is a ZIP archive containing `project.json` + media assets.

## Quick Verification

```bash
python scripts/scratch_utils.py  # Generates demo_project/ + demo_project.sb3
```

## Project Architecture

Three-layer Python library (zero external deps, Python 3.7+):

| Layer | Module | Purpose |
|-------|--------|---------|
| 1 | `scripts/scratch_utils.py` | Low-level: pack/unpack/validate .sb3 files |
| 2 | `scripts/block_builder.py` | Fluent builder: 60+ `make_*()` functions, `ScriptBuilder` |
| 3 | `scripts/project_builder.py` | High-level: `ScratchProject` class for complete projects |

Supporting resources:
- `SKILL.md` — Primary skill definition (Claude Code auto-detects this)
- `references/` — 17 files documenting all 194+ Scratch block opcodes with JSON examples
- `templates/` — 10 project templates (animation, games, interactive stories)

## Core Workflow

### Create a new project

```python
import sys; sys.path.insert(0, 'scripts')
from project_builder import ScratchProject
from block_builder import num, string

proj = ScratchProject()
stage = proj.create_stage()
cat = proj.create_sprite("Cat", x=0, y=0)

# when flag clicked → forever → move 10 steps → if on edge bounce
proj.add_blocks_from_chain(cat, [
    ("event_whenflagclicked", {}, {}),
    ("control_forever", {"SUBSTACK": [2, "NEXT"]}, {}),
    ("motion_movesteps", {"STEPS": num(10)}, {}),
    ("motion_ifonedgebounce", {}, {}),
])

proj.save_json("output/project.json")
```

### Modify existing .sb3

```python
from scratch_utils import unpack_sb3, create_project_directory, pack_sb3
project_dir, data = unpack_sb3('input.sb3')
# ... modify data dict ...
create_project_directory(data, project_dir)
pack_sb3(project_dir, 'output.sb3')
```

### Use a template

Read `templates/XX-name/README.md`, adapt to user requirements, generate `.sb3`.

## Block Reference Index

Before writing any block JSON, read the relevant reference file:

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
  "inputs": { "STEPS": [1, [4, "10"]] },
  "fields": {},
  "shadow": false, "topLevel": true,
  "x": 0, "y": 0
}
```

### Input Value Types

| Format | Meaning |
|--------|---------|
| `[1, [4, "10"]]` | Number (subtype 4) |
| `[1, [5, "10"]]` | Positive integer |
| `[1, [6, "10"]]` | Positive number |
| `[1, [7, "10"]]` | Integer |
| `[1, [8, "90"]]` | Angle |
| `[1, [10, "text"]]` | String literal |
| `[1, [12, "varId", "name"]]` | Variable reference |
| `[2, "blockId"]` | Nested reporter block |
| `[3, "blockId", [10, "default"]]` | Reporter with default fallback |

## Coordinate System

- Stage: 480×360 px
- x ∈ [-240, 240], y ∈ [-180, 180]
- Center at (0, 0)
- Direction: 0° = up, 90° = right, 180° = down, -90° = left

## Key API Reference

**scratch_utils.py**: `unpack_sb3()`, `pack_sb3()`, `create_empty_project()`, `add_sprite()`, `create_block()`, `add_block_to_target()`, `create_simple_script()`, `validate_project()`, `create_project_directory()`, `create_demo_project()`

**block_builder.py convenience functions**: `make_event_whenflagclicked()`, `make_event_whenkeypressed(key)`, `make_movesteps(n)`, `make_turnright(d)`, `make_gotoxy(x,y)`, `make_glidesecstoxy(s,x,y)`, `make_say(msg)`, `make_think(msg)`, `make_wait(s)`, `make_repeat(n)`, `make_forever()`, `make_if()`, `make_if_else()`, `make_create_clone_of(target)`, `make_broadcast(name)`, `make_play_sound(name)`, `make_ask(question)`, `make_pen_down()`, `make_setpencolor(hex)`, `ScriptBuilder`

**project_builder.py ScratchProject**: `create_stage()`, `create_sprite(name)`, `add_variable(target, name, val)`, `add_list(target, name)`, `add_broadcast(target, name)`, `add_costume(target, name)`, `add_sound(target, name)`, `add_block(target, opcode, inputs, fields)`, `add_blocks_from_chain(target, blocks)`, `add_extension(name)`, `to_dict()`, `save_json(path)`, `validate()`, `quick_project()`

## Best Practices

1. Read the relevant `references/blocks-*.md` before writing blocks — each file has complete JSON examples
2. Start simple, validate with `validate_project()` frequently
3. Use meaningful names: `score`, `lives`, `speed` (not `var1`, `var2`)
4. Keep sprite scripts independent; use broadcasts for inter-sprite communication
5. Test generated `.sb3` files in the Scratch editor
6. Python scripts are Python 3.7+, zero external deps — works on any machine

## Constraints

- .sb3 is a ZIP — `project.json` must be at archive root
- Each sprite needs ≥ 1 costume; Stage needs ≥ 1 backdrop
- Extensions require entries in `project.json` → `extensions` array
- Scratch online limit: 50 MB per project
- Media assets need `assetId` (MD5 hash) and `md5ext` fields
