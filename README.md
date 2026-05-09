# Catering Website (FastAPI + Railway)

Simple catering menu website built with FastAPI.

It renders 5 sample food items on a clean landing page and is ready to deploy on Railway.

## Features

- FastAPI backend
- Jinja template frontend
- Static CSS styling
- Railway deployment config included

## Run Locally

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
uvicorn main:app --reload
```

4. Open in your browser:

```text
http://127.0.0.1:8000
```

## Deploy To Railway

1. Push this repo to GitHub.
2. In Railway, create a new project and choose "Deploy from GitHub repo".
3. Select this repository.
4. Railway will detect the Python app and use `railway.json`.
5. Once deployed, open the generated Railway URL.

## Project Structure

```text
.
├── main.py
├── requirements.txt
├── railway.json
├── static/
│   └── styles.css
└── templates/
	└── index.html
```