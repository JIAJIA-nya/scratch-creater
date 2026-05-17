# GitHub Copilot Instructions — Scratch Creator

This repository is an AI Agent Skill for creating and modifying MIT Scratch 3.0 projects (`.sb3` files). `.sb3` files are ZIP archives containing `project.json` and media assets (SVG/PNG costumes, WAV/MP3 sounds).

## What This Project Provides

- **`SKILL.md`** — Primary skill definition with complete workflow
- **`references/`** — 17 Markdown files documenting all 194+ Scratch 3.0 block opcodes with JSON examples
- **`scripts/`** — Python modules (zero external dependencies, Python 3.7+ stdlib only) for building, packing, and validating .sb3 files
- **`templates/`** — 10 project templates (animation, games, interactive stories)

## How to Help Users Create Scratch Projects

When a user asks to create or modify a Scratch project:

1. **Understand requirements** — project type (animation, game, story), complexity, needed sprites and extensions
2. **Consult block references** — read the relevant `references/blocks-*.md` file(s) for the needed block opcodes
3. **Generate Python code** — use `scripts/project_builder.py` and `scripts/block_builder.py`
4. **Pack the project** — use `scripts/scratch_utils.py` to create the `.sb3` file

## Block Reference Index

| Category | Blocks | Reference File |
|----------|--------|----------------|
| Events | 10 | `references/blocks-events.md` |
| Motion | 18 | `references/blocks-motion.md` |
| Looks | 24 | `references/blocks-looks.md` |
| Sound | 12 | `references/blocks-sound.md` |
| Control | 17 | `references/blocks-control.md` |
| Sensing | 20 | `references/blocks-sensing.md` |
| Operators | 18 | `references/blocks-operators.md` |
| Variables & Lists | 17 | `references/blocks-variables.md` |
| Music extension | 7 | `references/blocks-music.md` |
| Pen extension | 11 | `references/blocks-pen.md` |
| Video Sensing | 3 | `references/blocks-video.md` |
| Translate | 2 | `references/blocks-translate.md` |
| Text to Speech | 3 | `references/blocks-texttospeech.md` |
| micro:bit | 16 | `references/blocks-microbit.md` |
| LEGO | 12+ | `references/blocks-lego.md` |
| Custom Blocks | 4 | `references/blocks-custom.md` |
| Project Schema | — | `references/project-json-schema.md` |

## Block JSON Format

Each block is a JSON object in the target's `blocks` dictionary:

```json
{
  "opcode": "motion_movesteps",
  "next": null,
  "parent": null,
  "inputs": { "STEPS": [1, [4, "10"]] },
  "fields": {},
  "shadow": false,
  "topLevel": true,
  "x": 0,
  "y": 0
}
```

**Input value formats:**
- `[1, [4, "10"]]` — Number literal (4=number, 5=positive int, 6=positive num, 7=integer, 8=angle)
- `[1, [10, "text"]]` — String literal
- `[1, [12, "varId", "varName"]]` — Variable reference
- `[2, "blockId"]` — Nested reporter block
- `[3, "blockId", [10, "default"]]` — Reporter with default value

## Coordinate System

- Stage: 480 × 360 pixels
- x range: [-240, 240]
- y range: [-180, 180]
- Center: (0, 0)
- Direction: 0° = up, 90° = right, 180° = down, -90° = left

## Python Modules Quick Reference

### scratch_utils.py
`unpack_sb3()`, `pack_sb3()`, `create_empty_project()`, `add_sprite()`, `add_backdrop()`, `create_block()`, `add_block_to_target()`, `create_simple_script()`, `validate_project()`, `create_project_directory()`, `create_demo_project()`

### block_builder.py
Key builders: `make_event_whenflagclicked()`, `make_event_whenkeypressed(key)`, `make_movesteps(n)`, `make_gotoxy(x,y)`, `make_say(msg)`, `make_think(msg)`, `make_wait(secs)`, `make_repeat(n)`, `make_forever()`, `make_if()`, `make_if_else()`, `make_broadcast(name)`, `make_create_clone_of(target)`, `make_pen_down()`, `make_play_sound(name)`

Input helpers: `num(v)`, `string(v)`, `variable_ref(name, id)`, `block_ref(id)`, `block_ref_default(id, default)`

### project_builder.py
`ScratchProject` class: `create_stage()`, `create_sprite(name, x, y)`, `add_variable(target, name, val)`, `add_list(target, name)`, `add_broadcast(target, name)`, `add_costume(target, name)`, `add_sound(target, name)`, `add_blocks_from_chain(target, blocks)`, `add_extension(name)`, `save_json(path)`, `validate()`

## Templates (10)
01-simple-animation, 02-bouncing-ball, 03-quiz-game, 04-platformer, 05-maze-game, 06-pong, 07-flappy-bird, 08-interactive-story, 09-paint-app, 10-multiplayer-chat. Each has a `README.md` with concept, required blocks, and sprite requirements.

## Constraints
- Every sprite ≥ 1 costume; Stage ≥ 1 backdrop
- Extensions must be in `project.json` `extensions` array
- `.sb3` = ZIP archive; `project.json` at root
- 50 MB limit on Scratch online
- Python 3.7+, zero external deps
