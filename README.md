
# Advanced Enhanced Multi-Cloud Control Plane (MSc Dissertation)

## Setup
1. Extract ZIP
2. Open folder in VS Code
3. Create virtual environment:
   python -m venv .venv
   source .venv/bin/activate (Mac/Linux)
   .venv\Scripts\Activate.ps1 (Windows)

4. Install dependencies:
   pip install -r requirements.txt

## Run CLI
python -m app.main

## Run API
uvicorn app.api:app --reload
Open: http://127.0.0.1:8000/docs
