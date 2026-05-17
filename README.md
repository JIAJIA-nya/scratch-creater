# Scratch Creator Skill

> Let AI Agents help you create and modify MIT Scratch 3.0 projects (.sb3 files).

**中文版本**: [README_cn.md](README_cn.md)

---

## Table of Contents

- [What is this?](#what-is-this)
- [Features](#features)
- [Compatible Agents](#compatible-agents)
- [Requirements](#requirements)
- [Installation](#installation)
- [Directory Structure](#directory-structure)
- [Quick Start](#quick-start)
  - [Creating a New Project](#creating-a-new-project)
  - [Modifying an Existing Project](#modifying-an-existing-project)
  - [Using Templates](#using-templates)
  - [Running the Scripts Directly](#running-the-scripts-directly)
- [Project Workflow](#project-workflow)
  - [Step 1: Requirements Analysis](#step-1-requirements-analysis)
  - [Step 2: Creating a New Project](#step-2-creating-a-new-project)
  - [Step 3: Modifying an Existing Project](#step-3-modifying-an-existing-project)
  - [Step 4: Using Templates](#step-4-using-templates)
- [Understanding .sb3 Files](#understanding-sb3-files)
  - [File Format](#file-format)
  - [project.json Structure](#projectjson-structure)
  - [Block JSON Format](#block-json-format)
  - [Input Value Types](#input-value-types)
  - [Coordinate System](#coordinate-system)
- [Block Reference](#block-reference)
- [Python Scripts API](#python-scripts-api)
  - [scratch_utils.py](#scratchutilspy)
  - [block_builder.py](#blockbuilderpy)
  - [project_builder.py](#projectbuilderpy)
- [Templates](#templates)
- [Best Practices](#best-practices)
- [Limitations](#limitations)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

---

## What is this?

Scratch Creator is an AI Agent Skill that enables Claude, Codex, OpenCode, and other AI coding assistants to programmatically create, modify, and package Scratch 3.0 projects. Instead of manually dragging blocks in the Scratch editor, you can describe what you want in natural language and let the Agent generate the project file for you.

Scratch 3.0 is developed by MIT and used by millions of children and educators worldwide. Its .sb3 file format is an open standard — a ZIP archive containing a `project.json` and media assets. This Skill provides everything an AI Agent needs to work with that format.

---

## Features

- **Create from scratch** — Generate complete .sb3 projects from a text description
- **Modify existing projects** — Unpack, edit, and repackage .sb3 files
- **Full block coverage** — Reference documentation for 194+ block opcodes across all categories and extensions
- **Python utilities** — Scripts for packing, unpacking, validating, and building projects programmatically
- **Project templates** — 10 ready-made templates for common project types (animation, games, interactive stories, etc.)
- **Cross-agent compatibility** — Works with any AI Agent that can read files and execute code

---

## Compatible Agents

This Skill is provided as Markdown documents + Python scripts. Theoretically, **any AI Agent that supports file reading and code execution** can use it:

| Agent | Compatibility | Notes |
|-------|--------------|-------|
| **Claude (Cowork)** | Perfect | Native SKILL.md support, can read `references/` directly |
| **Claude Code** | Perfect | SKILL.md is Claude Code's native skill format |
| **OpenAI Codex** | Usable | Read SKILL.md + `references/` as context, execute Python scripts |
| **OpenCode** | Usable | Same — supports Markdown context and script execution |
| **Cursor** | Usable | Add SKILL.md and `references/` to project context |
| **GitHub Copilot** | Partial | Can use SKILL.md as context reference, but cannot execute scripts directly |
| **Gemini CLI** | Usable | Any agent that supports reading files and executing commands |

**Core principle:** The `SKILL.md` and `references/` directory provide complete Scratch 3.0 block reference documentation. After reading them, the Agent gains all opcode knowledge needed to generate correct project JSON. The `scripts/` directory provides Python utility functions that the Agent can call directly or translate into other languages.

---

## Requirements

- **Python 3.7+** — For running the utility scripts
- **No external dependencies** — The scripts use only Python standard library modules (`zipfile`, `json`, `os`, `uuid`, `hashlib`, `shutil`)
- **An AI Agent** — Claude Code, Claude Cowork, Codex, OpenCode, Cursor, etc.

---

## Installation

### As a Skill for Claude Code / Claude Cowork

1. Clone or download this repository to your project directory or skills directory.
2. The Agent will automatically detect `SKILL.md` and use it as a skill.

```bash
git clone https://github.com/your-repo/scratch-creator.git
```

### As a Standalone Python Library

1. Clone the repository.
2. Copy or symlink the `scripts/` directory into your project.
3. Import and use the modules directly:

```python
import sys
sys.path.insert(0, 'scripts')
from scratch_utils import create_demo_project, pack_sb3, unpack_sb3, validate_project
from block_builder import make_movesteps, make_say, ScriptBuilder
from project_builder import ScratchProject, quick_project
```

### Development Setup

```bash
# Clone the repository
git clone https://github.com/your-repo/scratch-creator.git
cd scratch-creator

# No pip install needed — zero external dependencies
# Verify it works:
python -c "from scripts.scratch_utils import create_demo_project, validate_project; p = create_demo_project(); print('Valid:', validate_project(p)[0])"
```

---

## Directory Structure

```
scratch-creator/
├── SKILL.md                        # Agent skill definition (workflow & usage)
├── README.md                       # This file (English documentation)
├── README_cn.md                    # Chinese documentation
├── references/                     # Complete block reference docs (194+ opcodes)
│   ├── blocks-events.md            # Event blocks (10)
│   ├── blocks-motion.md            # Motion blocks (18)
│   ├── blocks-looks.md             # Looks blocks (24)
│   ├── blocks-sound.md             # Sound blocks (12)
│   ├── blocks-control.md           # Control blocks (17)
│   ├── blocks-sensing.md           # Sensing blocks (20)
│   ├── blocks-operators.md         # Operators (18)
│   ├── blocks-variables.md         # Variables & Lists (17)
│   ├── blocks-music.md             # Music extension (7)
│   ├── blocks-pen.md               # Pen extension (11)
│   ├── blocks-video.md             # Video Sensing extension (3)
│   ├── blocks-translate.md         # Translate extension (2)
│   ├── blocks-texttospeech.md      # Text to Speech extension (3)
│   ├── blocks-microbit.md          # micro:bit extension (16)
│   ├── blocks-lego.md              # LEGO extension (12+)
│   ├── blocks-custom.md            # Custom blocks (My Blocks) (4)
│   └── project-json-schema.md      # Complete project.json structure reference
├── scripts/                        # Python utility scripts (zero dependencies)
│   ├── __init__.py                 # Package marker
│   ├── scratch_utils.py            # Pack/unpack/validate .sb3 files
│   ├── block_builder.py            # Fluent block & script builder
│   └── project_builder.py          # High-level project builder
└── templates/                      # Project templates (10)
    ├── 01-simple-animation/        # Simple animation (with example project.json)
    │   ├── project.json            # Complete working project
    │   └── README.md               # Template description
    ├── 02-bouncing-ball/           # Bouncing ball with gravity
    ├── 03-quiz-game/               # Quiz game
    ├── 04-platformer/              # Platformer game
    ├── 05-maze-game/               # Maze game
    ├── 06-pong/                    # Pong game
    ├── 07-flappy-bird/             # Flappy Bird
    ├── 08-interactive-story/       # Interactive story
    ├── 09-paint-app/               # Paint/drawing app
    └── 10-multiplayer-chat/        # Multiplayer chat simulation
```

---

## Quick Start

### Creating a New Project

Tell the Agent:

> "Help me create a Scratch game where the player uses arrow keys to move a character and collect stars"

The Agent will:
1. Read `SKILL.md` to understand the workflow
2. Read relevant block reference docs (motion, events, control, etc.)
3. Use `scripts/project_builder.py` to create the project structure
4. Use `scripts/block_builder.py` to write block scripts
5. Use `scripts/scratch_utils.py` to pack into an .sb3 file
6. Validate the output with `validate_project()`

### Modifying an Existing Project

> "Make the character in this .sb3 file move faster"

The Agent will:
1. Unpack the .sb3 file using `unpack_sb3()`
2. Read and analyze `project.json`
3. Read the relevant block reference to confirm the correct opcode
4. Modify the block parameters (e.g., change the `STEPS` input value)
5. Repack using `pack_sb3()`

### Using Templates

> "Use the platformer template to create a new game"

The Agent will:
1. Read the template description in `templates/04-platformer/README.md`
2. Adapt the template to the user's requirements
3. Generate a complete .sb3 file

### Running the Scripts Directly

You can also use the Python scripts directly without an AI Agent:

```python
import sys
sys.path.insert(0, 'scripts')
from scratch_utils import create_demo_project, pack_sb3, validate_project, create_project_directory

# Create a demo project
project = create_demo_project()

# Validate it
is_valid, issues = validate_project(project)
print(f"Valid: {is_valid}")

# Save as .sb3
create_project_directory(project, 'my_project')
pack_sb3('my_project', 'my_project.sb3')
print("Created my_project.sb3")
```

---

## Project Workflow

### Step 1: Requirements Analysis

Before creating a project, understand:

- **Project type**: Animation, game, interactive story, or educational demo?
- **Target audience**: Children learning, classroom teaching, or personal project?
- **Complexity**: Simple demo or full game?
- **Existing assets**: Does the user have media files to import?
- **Extensions needed**: Music, pen, video sensing, translate, micro:bit, LEGO?

### Step 2: Creating a New Project

1. Read `references/project-json-schema.md` to understand the full structure
2. Read the relevant block reference docs based on project type (see [Block Reference](#block-reference) index)
3. Use `scripts/project_builder.py` to create the project structure
4. Use `scripts/block_builder.py` to write block scripts
5. Use `scripts/scratch_utils.py` to pack into .sb3

### Step 3: Modifying an Existing Project

1. **Unpack** the .sb3: `unpack_sb3('file.sb3')` → returns `(project_dir, project_data)`
2. **Read** project.json: analyze targets, blocks, and media
3. **Read** the relevant block reference doc to confirm opcodes
4. **Modify** project.json (change inputs, fields, add/remove blocks)
5. **Repack**: `pack_sb3(project_dir, 'output.sb3')`

### Step 4: Using Templates

1. Read the template's `README.md` in `templates/XX-name/`
2. Customize based on user requirements
3. Generate the .sb3 file

---

## Understanding .sb3 Files

### File Format

An .sb3 file is a ZIP archive containing:
- `project.json` — Core project data (sprites, backdrops, scripts, variables)
- Media files — SVG/PNG costumes, WAV/MP3 sounds (referenced by hash)

### project.json Structure

```json
{
  "targets": [ /* Stage + Sprites */ ],
  "monitors": [ /* Variable watchers */ ],
  "extensions": [ /* Used extensions */ ],
  "meta": {
    "semver": "3.0.0",
    "vm": "0.2.0",
    "agent": "Mozilla/5.0 ..."
  }
}
```

Each **target** is either the Stage (isStage: true) or a Sprite (isStage: false). Each target contains:
- `variables` — `{varId: [name, value]}`
- `lists` — `{listId: [name, [items]]}`
- `broadcasts` — `{msgId: name}`
- `blocks` — `{blockId: blockData}`
- `costumes` — Array of costume descriptors
- `sounds` — Array of sound descriptors

### Block JSON Format

```json
{
  "blockId": {
    "opcode": "motion_movesteps",
    "next": "nextBlockId",
    "parent": "parentBlockId",
    "inputs": {
      "STEPS": [1, [4, "10"]]
    },
    "fields": {},
    "shadow": false,
    "topLevel": true,
    "x": 0,
    "y": 0
  }
}
```

- `opcode` — The block type identifier (e.g., `motion_movesteps`)
- `next` — ID of the block below (vertical stack connection)
- `parent` — ID of the block above
- `inputs` — Input slots (reporters, dropdowns)
- `fields` — Fixed field values (e.g., dropdown selections)
- `shadow` — `true` if this is a shadow block (default value that can't be replaced)
- `topLevel` — `true` if this is a hat block (script entry point)
- `x`, `y` — Position on the workspace

### Input Value Types

| Format | Meaning |
|--------|---------|
| `[1, [4, "10"]]` | Number literal |
| `[1, [10, "text"]]` | String literal |
| `[1, [12, "varId", "varName"]]` | Variable reference |
| `[2, "blockId"]` | Nested reporter (value from another block) |
| `[3, "blockId", [10, "default"]]` | Nested reporter with default fallback |

**Number subtypes:**
| Code | Type |
|------|------|
| `[4, N]` | Number |
| `[5, N]` | Positive integer |
| `[6, N]` | Positive number |
| `[7, N]` | Integer |
| `[8, N]` | Angle |

### Coordinate System

- Stage size: 480 × 360 pixels
- x range: [-240, 240]
- y range: [-180, 180]
- Center: (0, 0)
- Direction: 0° = up, 90° = right, 180° = down, -90° = left

---

## Block Reference

Complete opcode documentation for all Scratch 3.0 blocks:

| Category | Count | Reference File |
|----------|-------|----------------|
| Events | 10 | `references/blocks-events.md` |
| Motion | 18 | `references/blocks-motion.md` |
| Looks | 24 | `references/blocks-looks.md` |
| Sound | 12 | `references/blocks-sound.md` |
| Control | 17 | `references/blocks-control.md` |
| Sensing | 20 | `references/blocks-sensing.md` |
| Operators | 18 | `references/blocks-operators.md` |
| Variables & Lists | 17 | `references/blocks-variables.md` |
| Music (extension) | 7 | `references/blocks-music.md` |
| Pen (extension) | 11 | `references/blocks-pen.md` |
| Video Sensing (extension) | 3 | `references/blocks-video.md` |
| Translate (extension) | 2 | `references/blocks-translate.md` |
| Text to Speech (extension) | 3 | `references/blocks-texttospeech.md` |
| micro:bit (extension) | 16 | `references/blocks-microbit.md` |
| LEGO (extension) | 12+ | `references/blocks-lego.md` |
| Custom Blocks | 4 | `references/blocks-custom.md` |
| **Total** | **194+** | |

Each reference file contains:
- A table of all opcodes with names and descriptions
- Accepted field values and menus
- Complete JSON examples for every block

---

## Python Scripts API

### scratch_utils.py

Core utilities for .sb3 file manipulation. **Zero external dependencies.**

| Function | Description |
|----------|-------------|
| `unpack_sb3(sb3_path, output_dir=None)` | Unpack an .sb3 file into a directory. Returns `(project_dir, project_data)`. |
| `pack_sb3(project_dir, output_path)` | Pack a directory into an .sb3 file. |
| `create_empty_project()` | Create a minimal empty project dict (Stage only). |
| `add_sprite(project_data, name, x=0, y=0, ...)` | Add a sprite to the project. Returns the sprite dict. |
| `add_backdrop(stage, name, svg_content=None)` | Add a backdrop to the Stage. |
| `create_block(opcode, inputs, fields, ...)` | Create a single block dict. Returns `(block_id, block_dict)`. |
| `add_block_to_target(target, block_id, block_dict)` | Add a block to a target. |
| `create_simple_script(target, blocks_list)` | Chain blocks into a script. Returns first block ID. |
| `validate_project(project_data)` | Validate project integrity. Returns `(is_valid, issues)`. |
| `create_project_directory(project_data, output_dir, media_files=None)` | Write project to disk. |
| `create_demo_project()` | Create a demo project (green flag → say "你好" → move). |
| `generate_block_id()` | Generate a random block ID. |
| `num(value)` | Create a number input: `[1, [4, str(value)]]` |
| `str_input(value)` | Create a string input: `[1, [10, str(value)]]` |
| `var_ref(variable_name, var_id)` | Create a variable reference input. |
| `block_ref(block_id)` | Create a nested reporter reference: `[2, block_id]` |
| `block_ref_with_default(block_id, default)` | Reporter with default fallback: `[3, block_id, [10, default]]` |
| `field_value(value)` | Create a field value: `[value, None]` |

**Command-line usage:**
```bash
python scripts/scratch_utils.py
# Creates demo_project/ directory and demo_project.sb3
```

### block_builder.py

Fluent builder for creating individual blocks and scripts. Each function returns a `BlockBuilder` or `ScriptBuilder` object.

**Convenience block builders (selected):**

| Function | Block |
|----------|-------|
| `make_event_whenflagclicked()` | when flag clicked |
| `make_event_whenkeypressed(key)` | when key pressed |
| `make_event_whenbroadcastreceived(name, id)` | when I receive |
| `make_broadcast(name, id)` | broadcast |
| `make_movesteps(steps)` | move N steps |
| `make_turnright(degrees)` / `make_turnleft(degrees)` | turn right/left |
| `make_gotoxy(x, y)` / `make_glidesecstoxy(secs, x, y)` | go to / glide |
| `make_pointindirection(dir)` / `make_pointtowards(target)` | point in direction / towards |
| `make_say(msg)` / `make_sayforseconds(msg, secs)` | say / say for N secs |
| `make_think(msg)` | think |
| `make_show()` / `make_hide()` | show / hide |
| `make_nextcostume()` / `make_switchcostumeto(name)` | next costume / switch costume |
| `make_changesizeby(n)` / `make_setsizeto(n)` | change size / set size |
| `make_changeeffectby(effect, n)` / `make_seteffectto(effect, n)` | change/set effect |
| `make_wait(secs)` | wait N seconds |
| `make_repeat(n)` / `make_forever()` | repeat N / forever |
| `make_if()` / `make_if_else()` | if / if-else |
| `make_stop_all()` / `make_stop_this()` | stop all / stop this script |
| `make_start_as_clone()` | when I start as a clone |
| `make_create_clone_of(target)` | create clone of |
| `make_play_sound(name)` / `make_playuntildone(name)` | play sound |
| `make_setinstrument(n)` / `make_playdrum(drum, beats)` | set instrument / play drum |
| `make_playnote(note, beats)` / `make_rest(beats)` | play note / rest |
| `make_settempo(bpm)` | set tempo |
| `make_ask(question)` | ask and wait |
| `make_pen_clear()` / `make_pen_down()` / `make_pen_up()` | pen clear/down/up |
| `make_setpencolor(hex)` / `make_setpensize(n)` | set pen color/size |

**Reporter blocks:** `reporter_add()`, `reporter_subtract()`, `reporter_multiply()`, `reporter_divide()`, `reporter_random()`, `reporter_gt()`, `reporter_lt()`, `reporter_equals()`, `reporter_and()`, `reporter_or()`, `reporter_not()`, `reporter_join()`, `reporter_letter_of()`, `reporter_length()`, `reporter_mod()`, `reporter_round()`, `reporter_mathop()`, `reporter_xposition()`, `reporter_yposition()`, `reporter_direction()`, `reporter_size()`, `reporter_volume()`, `reporter_answer()`, `reporter_mousex()`, `reporter_mousey()`, `reporter_loudness()`, `reporter_timer()`, `reporter_dayssince2000()`, `reporter_username()`, `reporter_current()`, `reporter_music_tempo()`

**Input helper functions:** `num()`, `positive_int()`, `positive_num()`, `integer()`, `angle()`, `string()`, `variable_ref()`, `block_ref()`, `block_ref_default()`, `field_val()`, `color_val()`

**ScriptBuilder example:**
```python
from block_builder import ScriptBuilder, make_event_whenflagclicked

script = ScriptBuilder()
script.add("event_whenflagclicked", is_top_level=True)
script.add("motion_movesteps", inputs={"STEPS": num(10)})
script.add("looks_say", inputs={"MESSAGE": string("Hello!")})
blocks = script.build()
# Add blocks to target["blocks"]
```

### project_builder.py

High-level project builder for creating complete Scratch projects programmatically.

**ScratchProject class:**

| Method | Description |
|--------|-------------|
| `create_stage(name="Stage")` | Create the Stage target |
| `create_sprite(name, x=0, y=0, size=100, direction=90)` | Create a sprite |
| `add_variable(target, var_name, initial_value=0)` | Add a variable. Returns var ID. |
| `add_list(target, list_name, initial_items=None)` | Add a list. Returns list ID. |
| `add_broadcast(target, msg_name)` | Add a broadcast message. Returns msg ID. |
| `add_costume(target, name, data_format="svg", ...)` | Add a costume to a target |
| `add_sound(target, name, data_format="wav", ...)` | Add a sound to a target |
| `add_block(target, opcode, inputs, fields, ...)` | Add a single block. Returns block ID. |
| `add_blocks_from_chain(target, blocks_list)` | Add a chain of connected blocks. |
| `add_extension(ext_name)` | Register an extension (e.g., `"pen"`, `"music"`) |
| `to_dict()` | Export as project.json dict |
| `save_json(filepath)` | Save project.json to file |
| `validate()` | Validate project. Returns `(is_valid, issues)`. |

**Convenience function:** `quick_project(sprite_name="Sprite1")` — Creates a minimal project with a Stage (blank backdrop) and one sprite (one costume), ready for adding scripts.

**Full example:**
```python
from project_builder import ScratchProject
from block_builder import num, string

proj = ScratchProject()

# Stage
stage = proj.create_stage()

# Player sprite
player = proj.create_sprite("Player", x=0, y=0)

# Add a score variable
score_id = proj.add_variable(stage, "score", 0)

# Script: when flag clicked → forever → move 10 steps → if on edge, bounce
proj.add_blocks_from_chain(player, [
    ("event_whenflagclicked", {}, {}),
    ("control_forever", {"SUBSTACK": [2, "move_block"]}, {}),
])

# Save
proj.save_json("my_game/project.json")
```

---

## Templates

10 project templates covering common Scratch project types. Each template includes a README describing the concept, required blocks, and sprite requirements.

| # | Template | Difficulty | Concepts |
|---|----------|------------|----------|
| 01 | [Simple Animation](templates/01-simple-animation/) | Beginner | Events, loops, costume switching, bounce |
| 02 | [Bouncing Ball](templates/02-bouncing-ball/) | Beginner | Gravity simulation, variables, bounce |
| 03 | [Quiz Game](templates/03-quiz-game/) | Beginner | Variables, conditionals, asking/answering |
| 04 | [Platformer](templates/04-platformer/) | Intermediate | Keyboard input, gravity, collision detection |
| 05 | [Maze Game](templates/05-maze-game/) | Intermediate | Keyboard input, collision, broadcasting |
| 06 | [Pong](templates/06-pong/) | Intermediate | Motion, collision, scoring, variables |
| 07 | [Flappy Bird](templates/07-flappy-bird/) | Intermediate | Gravity, cloning, collision, scoring |
| 08 | [Interactive Story](templates/08-interactive-story/) | Beginner | Broadcasting, backdrop switching, dialogue |
| 09 | [Paint App](templates/09-paint-app/) | Advanced | Pen extension, mouse input, cloning |
| 10 | [Multiplayer Chat](templates/10-multiplayer-chat/) | Advanced | Cloud variables, messaging, lists |

---

## Best Practices

1. **Start simple** — Create the basic structure first, then gradually add complexity
2. **Modular scripts** — Keep each sprite's behavior independent; communicate via broadcast messages
3. **Meaningful variable names** — Use descriptive names like `score`, `lives`, `speed`
4. **Use templates** — Start from the closest template and customize
5. **Validate early** — Run `validate_project()` after creation to catch structural issues
6. **Test iteratively** — Load the .sb3 in the Scratch editor to test, then fix issues
7. **Performance** — Avoid unnecessary computation in `forever` loops; use clones wisely
8. **Clean up clones** — Always use `delete this clone` when a clone is no longer needed

---

## Limitations

- .sb3 files are ZIP archives; `project.json` must be at the root (not in a subdirectory)
- Scratch online platform has a 50 MB project file size limit
- Every sprite must have at least one costume
- The Stage must have at least one backdrop
- Extensions must be declared in the `extensions` array of project.json
- Media files (costumes, sounds) need proper `assetId` and `md5ext` fields for the Scratch editor to recognize them
- This Skill generates the project JSON structure but does not create image/audio assets — those must be provided separately or use Scratch's built-in assets

---

## Resources

- [MIT Scratch](https://scratch.mit.edu/) — Official Scratch website
- [Scratch Wiki - File Format](https://en.scratch-wiki.info/wiki/Scratch_File_Format) — Detailed file format documentation
- [Scratch Wiki - Block Syntax](https://en.scratch-wiki.info/wiki/Scratch_File_Format/Block_Selection) — Block selection reference
- [Scratch 3.0 File Format (GitHub)](https://github.com/scratchfoundation/scratch-vm) — scratch-vm source code
- [Scratch Blocks](https://github.com/scratchfoundation/scratch-blocks) — Visual block editor

---

## Contributing

Contributions are welcome:
- New project templates
- Additional block reference documentation
- Script improvements or bug fixes
- Translations

---
