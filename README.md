# MedicalChatbot
## Medical Chatbot

A lightweight medical chatbot project for research and experimentation. This repository contains the application entrypoint, helper modules, prompts, and research artifacts used while developing the chatbot.

## Features
- Simple command-line / local web interface (see `app.py`)
- Reusable helper utilities in `src/`
- Reproducible environment via `requirements.txt` or Conda

## Requirements
- Python 3.8+
- Conda (recommended) or a virtual environment

## Recommended Setup (Conda)
1. Create the Conda environment (you already ran this):

```bash
conda create -n medicalBotENV python=3.10 -y
```

2. Activate the environment:

PowerShell:
```powershell
conda activate medicalBotENV
```

Or bash / WSL / Git Bash:
```bash
conda activate medicalBotENV
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Alternate Setup (venv)
If you prefer a local virtualenv, create and activate it and then install the requirements:

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Linux / macOS:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Running
Run the app entrypoint:

```bash
python app.py
```

Adjust command-line options or configuration as needed (see `app.py` and `src/`).

## Project Structure
- `app.py` — application entrypoint
- `requirements.txt` — pip dependencies
- `setup.py` — packaging helper (if used)
- `src/` — project source modules (`helper.py`, `prompt.py`)
- `research/` — notebooks and experiments
- `.venv/` or Conda env — local virtual environment (ignored by `.gitignore`)

## Development
- Use `flake8` / `black` / `isort` as desired (not included by default)
- Run unit tests (if added) with `pytest`

## Notes
- Keep any secrets or API keys out of the repository; add them to a `.env` file and ensure `.env` is ignored.

## License
See the `LICENSE` file in the repository root.

---
If you'd like, I can also detect and configure the VS Code interpreter to use your `medicalBotENV` Conda environment.
# MedicalChatbot