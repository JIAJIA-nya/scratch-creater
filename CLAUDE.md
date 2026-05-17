# CLAUDE.md

## Project Overview

Scratch Creator is an AI Agent Skill that enables AI coding assistants to programmatically create, modify, and package MIT Scratch 3.0 projects (`.sb3` files). Users describe what they want in natural language, and the agent generates a valid Scratch project file.

`.sb3` files are ZIP archives containing a `project.json` and media assets (SVG/PNG costumes, WAV/MP3 sounds).

## Architecture

Three Python layers, each building on the one below:

```
scripts/scratch_utils.py     # Layer 1: Low-level .sb3 manipulation (pack/unpack/validate)
scripts/block_builder.py     # Layer 2: Fluent block & script construction
scripts/project_builder.py   # Layer 3: High-level project assembly
```

**Zero external dependencies** — all scripts use only Python standard library (`zipfile`, `json`, `os`, `uuid`, `hashlib`, `shutil`).

## Directory Structure

```
CLAUDE.md                    # Claude Code project documentation (this file)
SKILL.md                     # Primary skill entry point (Claude Code auto-detects this)
README.md / README_cn.md     # Human-facing docs (English / Chinese)
.codex/CODEX.md              # OpenAI Codex CLI instructions
.cursor/rules/               # Cursor auto-applied rules
.gemini/GEMINI.md            # Gemini CLI project instructions
.github/copilot-instructions.md  # GitHub Copilot instructions
.opencode/AGENTS.md          # OpenCode project instructions
.windsurfrules               # Windsurf project rules
.continuerules               # Continue extension rules
.augment/rules/              # Augment agent rules
.amazonq/rules/              # Amazon Q development rules
references/                  # 17 files — complete block opcode reference (194+ blocks)
scripts/                     # Python tools — zero deps, stdlib only
templates/                   # 10 project templates (animation, games, interactive stories)
```

## Common Commands

```bash
# Generate and validate a demo project
python scripts/scratch_utils.py

# Quick verification that everything works
python -c "from scripts.scratch_utils import create_demo_project, validate_project; p = create_demo_project(); print('Valid:', validate_project(p)[0])"

# Unpack an existing .sb3 to inspect it
python -c "
import sys; sys.path.insert(0,'scripts')
from scratch_utils import unpack_sb3
project_dir, data = unpack_sb3('some_project.sb3')
print(f'Unpacked to: {project_dir}')
"
```

## Key Patterns

### Creating a Scratch project (standard workflow)

```python
import sys; sys.path.insert(0, 'scripts')
from project_builder import ScratchProject
from block_builder import num, string

proj = ScratchProject()
stage = proj.create_stage()
sprite = proj.create_sprite("Cat", x=0, y=0)

# Add a script: when flag clicked → move 10 steps → say "Hello!"
proj.add_blocks_from_chain(sprite, [
    ("event_whenflagclicked", {}, {}),
    ("motion_movesteps", {"STEPS": num(10)}, {}),
    ("looks_say", {"MESSAGE": string("Hello!")}, {}),
])

proj.save_json("my_project/project.json")
```

### Block JSON format

```json
{
  "blockId": {
    "opcode": "motion_movesteps",
    "next": null, "parent": null,
    "inputs": { "STEPS": [1, [4, "10"]] },
    "fields": {},
    "shadow": false, "topLevel": true,
    "x": 0, "y": 0
  }
}
```

Input types: `[1, [4, "10"]]` = number, `[1, [10, "text"]]` = string, `[1, [12, "varId", "name"]]` = variable ref, `[2, "blockId"]` = nested reporter.

### Coordinate system

Stage: 480×360 px. x ∈ [-240, 240], y ∈ [-180, 180], center at (0,0). Direction: 0° = up, 90° = right.

### Modifying an existing project

1. `unpack_sb3('file.sb3')` → `(project_dir, project_data)`
2. Modify `project_data` dict (add/change blocks, sprites, variables)
3. `create_project_directory(project_data, project_dir)` — write back to disk
4. `pack_sb3(project_dir, 'output.sb3')` — re-package

### Reading block references

When you need to use a specific Scratch block, read the corresponding file in `references/`. There are 17 files organized by category (events, motion, looks, sound, control, sensing, operators, variables, music, pen, video, translate, text-to-speech, micro:bit, LEGO, custom blocks, and the project.json schema). Each file contains complete opcode tables and JSON examples.

## Conventions

- **Python comments and docstrings are in Chinese** — the primary author is a Chinese speaker
- **Bilingual documentation** — README.md (EN) and README_cn.md (ZH) are both maintained
- **No package manager** — no `package.json`, `pyproject.toml`, or pip dependencies
- **Python 3.7+** required
- **SKILL.md is the primary entry point** — Claude Code auto-detects it as a skill

## Adding New Agent Platform Support

This project is document-driven — agents use it by reading Markdown files and executing Python scripts. To add support for a new platform:

1. Identify the platform's convention for project-level instructions (e.g., `.cursorrules`, `AGENTS.md`, `.github/copilot-instructions.md`)
2. Create the appropriate config file containing: project overview, core workflow, how to use the Python scripts, block reference index, and coordinate system
3. Add the platform to the compatibility tables in README.md and README_cn.md

Existing platform configs: `.codex/CODEX.md`, `.cursor/rules/`, `.gemini/GEMINI.md`, `.github/copilot-instructions.md`, `.opencode/AGENTS.md`, `.windsurfrules`, `.continuerules`, `.augment/rules/`, `.amazonq/rules/`.
