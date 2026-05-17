# Augment Rules — Scratch Creator

AI Agent Skill for creating and modifying MIT Scratch 3.0 projects (`.sb3` files).

## Project Capabilities

This project can programmatically generate complete Scratch 3.0 projects. It provides:
- Complete block reference documentation (194+ opcodes across 17 files in `references/`)
- Python build scripts (`scripts/` — zero external deps)
- Project templates (`templates/` — 10 game/animation templates)

## Workflow for Creating Scratch Projects

1. **Analyze** the user's request (project type, sprites, features)
2. **Read** relevant `references/blocks-*.md` for needed block opcodes
3. **Build** the project using `scripts/project_builder.py`
4. **Pack** into `.sb3` using `scripts/scratch_utils.py`

## Block Reference Quick Index

| Category | File | Count |
|----------|------|-------|
| Events | `references/blocks-events.md` | 10 |
| Motion | `references/blocks-motion.md` | 18 |
| Looks | `references/blocks-looks.md` | 24 |
| Sound | `references/blocks-sound.md` | 12 |
| Control | `references/blocks-control.md` | 17 |
| Sensing | `references/blocks-sensing.md` | 20 |
| Operators | `references/blocks-operators.md` | 18 |
| Variables & Lists | `references/blocks-variables.md` | 17 |
| Music | `references/blocks-music.md` | 7 |
| Pen | `references/blocks-pen.md` | 11 |
| Video Sensing | `references/blocks-video.md` | 3 |
| Translate | `references/blocks-translate.md` | 2 |
| Text to Speech | `references/blocks-texttospeech.md` | 3 |
| micro:bit | `references/blocks-microbit.md` | 16 |
| LEGO | `references/blocks-lego.md` | 12+ |
| Custom Blocks | `references/blocks-custom.md` | 4 |
| Schema | `references/project-json-schema.md` | — |

## Key Code Pattern

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
])
proj.save_json("output/project.json")
```

## Python API Essentials
- `scratch_utils.py`: `unpack_sb3()`, `pack_sb3()`, `create_empty_project()`, `add_sprite()`, `validate_project()`
- `block_builder.py`: `make_movesteps(n)`, `make_say(msg)`, `make_forever()`, `make_if()`, `ScriptBuilder`, `num()`, `string()`
- `project_builder.py`: `ScratchProject` (high-level), `quick_project()` (minimal starter)

## Block JSON Format
```json
{
  "opcode": "motion_movesteps",
  "inputs": {"STEPS": [1, [4, "10"]]},
  "fields": {},
  "shadow": false, "topLevel": true
}
```
Input: `[1,[4,"N"]]`=number, `[1,[10,"S"]]`=string, `[1,[12,"id","name"]]`=variable, `[2,"blockId"]`=nested.

## Coordinate System
Stage: 480×360. x:[-240,240], y:[-180,180]. 0°=up, 90°=right.

## Rules
- Read block reference files before writing block JSON
- Always validate with `validate_project()`
- Every sprite needs ≥ 1 costume; Stage needs ≥ 1 backdrop
- Extensions must be declared in project.json `extensions` array
