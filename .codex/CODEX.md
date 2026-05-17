# CODEX.md — Scratch Creator

AI Agent Skill for creating and modifying MIT Scratch 3.0 projects (`.sb3` files). Generate complete Scratch projects programmatically using Python scripts and block reference documentation.

## Quick Start

```bash
# Verify the project works
python scripts/scratch_utils.py
```

## Core Workflow

### Creating a new project
1. Read `references/project-json-schema.md` for the overall structure
2. Read block reference files for the categories you need (see index below)
3. Use `scripts/project_builder.py` to create project structure
4. Use `scripts/block_builder.py` to create block scripts
5. Use `scripts/scratch_utils.py` to pack into .sb3

### Modifying an existing project
1. `unpack_sb3('file.sb3')` → `(project_dir, project_data)`
2. Edit `project_data` dict
3. Write back with `create_project_directory(project_data, project_dir)`
4. `pack_sb3(project_dir, 'output.sb3')`

### Using templates
Read `templates/XX-name/README.md`, adapt to user needs, generate .sb3.

## Python API Summary

**scratch_utils.py** — Pack/unpack/validate
- `unpack_sb3(path)` → `(dir, data)`
- `pack_sb3(dir, path)`
- `create_empty_project()` → dict
- `add_sprite(project, name, x, y)` → sprite dict
- `create_block(opcode, inputs, fields)` → `(id, dict)`
- `validate_project(data)` → `(bool, issues[])`
- `create_project_directory(data, dir)`

**block_builder.py** — 60+ `make_*()` convenience functions + `ScriptBuilder`
- `make_event_whenflagclicked()`, `make_movesteps(n)`, `make_say(msg)`, `make_wait(secs)`, `make_forever()`, `make_if()`, `make_repeat(n)`, etc.
- Reporter blocks: `reporter_add()`, `reporter_random()`, `reporter_xposition()`, etc.
- Input helpers: `num(v)`, `string(v)`, `variable_ref(name, id)`, `block_ref(id)`

**project_builder.py** — `ScratchProject` class
- `create_stage()`, `create_sprite(name)`
- `add_variable(target, name, value)` → id
- `add_costume(target, name, format)`, `add_sound(target, name, format)`
- `add_blocks_from_chain(target, [(opcode, inputs, fields), ...])`
- `add_extension(name)` — e.g. `"pen"`, `"music"`
- `save_json(path)`, `validate()` → `(bool, issues)`

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

### Input types
| Format | Meaning |
|--------|---------|
| `[1, [4, "10"]]` | Number literal |
| `[1, [10, "text"]]` | String literal |
| `[1, [12, "varId", "name"]]` | Variable ref |
| `[2, "blockId"]` | Nested reporter |
| `[3, "blockId", [10, "default"]]` | Reporter with default |

## Block Reference Index (194+ blocks)

| Category | File |
|----------|------|
| Events (10) | `references/blocks-events.md` |
| Motion (18) | `references/blocks-motion.md` |
| Looks (24) | `references/blocks-looks.md` |
| Sound (12) | `references/blocks-sound.md` |
| Control (17) | `references/blocks-control.md` |
| Sensing (20) | `references/blocks-sensing.md` |
| Operators (18) | `references/blocks-operators.md` |
| Variables & Lists (17) | `references/blocks-variables.md` |
| Music (7) | `references/blocks-music.md` |
| Pen (11) | `references/blocks-pen.md` |
| Video Sensing (3) | `references/blocks-video.md` |
| Translate (2) | `references/blocks-translate.md` |
| Text to Speech (3) | `references/blocks-texttospeech.md` |
| micro:bit (16) | `references/blocks-microbit.md` |
| LEGO (12+) | `references/blocks-lego.md` |
| Custom (4) | `references/blocks-custom.md` |
| Schema | `references/project-json-schema.md` |

## Coordinate System

Stage: 480×360 px. x ∈ [-240, 240], y ∈ [-180, 180]. Center: (0,0). Direction: 0° = up, 90° = right, 180° = down, -90° = left.

## Templates (10)

01-simple-animation, 02-bouncing-ball, 03-quiz-game, 04-platformer, 05-maze-game, 06-pong, 07-flappy-bird, 08-interactive-story, 09-paint-app, 10-multiplayer-chat.

Each template folder contains a `README.md` describing the concept, required blocks, and sprite requirements.

## Best Practices
1. Start simple, add complexity incrementally
2. Keep sprite behaviors independent; communicate via broadcasts
3. Use meaningful variable names (`score`, `lives`, `speed`)
4. Validate with `validate_project()` after every change
5. Test in the Scratch editor after generating
