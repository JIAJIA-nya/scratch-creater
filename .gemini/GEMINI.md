# GEMINI.md — Scratch Creator

Scratch Creator is an AI Agent Skill for creating and modifying MIT Scratch 3.0 projects (`.sb3` files). `.sb3` files are ZIP archives containing `project.json` and media assets.

## How to Use This Project

You have three tools at your disposal:

1. **`references/`** — 17 Markdown files documenting all 194+ Scratch block opcodes with JSON examples. Read these BEFORE writing any block JSON.
2. **`scripts/`** — Python modules (zero deps, stdlib only) for building, packing, and validating .sb3 files.
3. **`templates/`** — 10 project templates (animation, games, stories) with concept descriptions in `README.md` files.

## Workflow

### To create a new Scratch project:

1. **Understand the user's requirements** — project type (animation/game/story), complexity, needed extensions
2. **Read `references/project-json-schema.md`** for the structure of `project.json`
3. **Read relevant block reference files** — check the index below for which file covers which category
4. **Use `project_builder.py` + `block_builder.py`** to construct the project
5. **Pack with `scratch_utils.py`** into an `.sb3` file

### Example: Creating a simple project

```python
import sys; sys.path.insert(0, 'scripts')
from project_builder import ScratchProject
from block_builder import num, string

proj = ScratchProject()
stage = proj.create_stage()
sprite = proj.create_sprite("Cat")

proj.add_blocks_from_chain(sprite, [
    ("event_whenflagclicked", {}, {}),
    ("motion_movesteps", {"STEPS": num(10)}, {}),
    ("looks_say", {"MESSAGE": string("Hello!")}, {}),
])

proj.save_json("my_project/project.json")
```

Then pack: `python scripts/scratch_utils.py` (or call `pack_sb3()` directly).

### To modify an existing .sb3:

1. `unpack_sb3('file.sb3')` → `(project_dir, project_data)`
2. Edit the `project_data` dict (add/change blocks, sprites, variables)
3. `create_project_directory(project_data, project_dir)`
4. `pack_sb3(project_dir, 'output.sb3')`

## Block Reference Index

| Category (count) | Reference File |
|------------------|----------------|
| Events (10) | `references/blocks-events.md` |
| Motion (18) | `references/blocks-motion.md` |
| Looks (24) | `references/blocks-looks.md` |
| Sound (12) | `references/blocks-sound.md` |
| Control (17) | `references/blocks-control.md` |
| Sensing (20) | `references/blocks-sensing.md` |
| Operators (18) | `references/blocks-operators.md` |
| Variables & Lists (17) | `references/blocks-variables.md` |
| Music extension (7) | `references/blocks-music.md` |
| Pen extension (11) | `references/blocks-pen.md` |
| Video Sensing (3) | `references/blocks-video.md` |
| Translate (2) | `references/blocks-translate.md` |
| Text to Speech (3) | `references/blocks-texttospeech.md` |
| micro:bit (16) | `references/blocks-microbit.md` |
| LEGO (12+) | `references/blocks-lego.md` |
| Custom blocks (4) | `references/blocks-custom.md` |
| Project schema | `references/project-json-schema.md` |

## Key Python Modules

- **`scratch_utils.py`** — `unpack_sb3()`, `pack_sb3()`, `create_empty_project()`, `add_sprite()`, `create_block()`, `validate_project()`, `create_project_directory()`
- **`block_builder.py`** — `make_movesteps()`, `make_say()`, `make_forever()`, `make_if()`, `ScriptBuilder`, reporter blocks, input helpers (`num()`, `string()`, `variable_ref()`)
- **`project_builder.py`** — `ScratchProject` class: `create_sprite()`, `add_variable()`, `add_blocks_from_chain()`, `add_extension()`, `save_json()`, `validate()`

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

Input types: `[1, [4, "10"]]` = number, `[1, [10, "text"]]` = string, `[1, [12, "varId", "name"]]` = variable, `[2, "blockId"]` = nested reporter.

## Coordinate System

Stage: 480×360. x: [-240, 240], y: [-180, 180], center: (0,0). Direction: 0° = up, 90° = right.

## Constraints
- Every sprite needs ≥ 1 costume; Stage needs ≥ 1 backdrop
- Extensions must be declared in `project.json` → `extensions` array
- .sb3 online limit: 50 MB
- Python 3.7+ required, zero external dependencies
