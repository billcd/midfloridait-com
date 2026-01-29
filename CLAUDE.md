# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MidFloridaIT.com — Flask web application for Mid Florida IT, an informational site with planned Stripe payment portal.

## Environment

- Python 3.12.3 via virtualenv at `.venv/`
- Activate: `source .venv/bin/activate`
- IDE: PyCharm

## Running Locally

```bash
source .venv/bin/activate
python app.py
```

Site runs at http://localhost:5001 (port 5000 is used by macOS AirPlay Receiver).

## Project Structure

- `app.py` — Flask application entry point
- `templates/` — Jinja2 HTML templates
- `static/css/` — Stylesheets
- `tests/` — Pytest test suite
- `Procfile` — Heroku process definition (gunicorn)
- `requirements.txt` — Python dependencies (pip freeze)

## Testing

```bash
source .venv/bin/activate
python -m pytest tests/ -v
```

## Deployment

- **GitHub remote:** `origin` (git@github.com:billcd/midfloridait-com.git)
- **Heroku remote:** `heroku` (midfloridait-com)
- Push to Heroku: `git push heroku master`
