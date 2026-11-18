# AI Art Official Website (`aiart.io`)

Official marketing and landing website for **AI Art**, showcasing the AI Art Trading Bot, historical monthly return chart, pricing tiers, waitlist registration guide, and company/legal pages.

## Architecture Overview

This repository serves a server-rendered marketing site with no database or backend authentication (waitlist and contact actions link out to external services):

- **Web Server (`ai_art_landing/`)**: Python **FastAPI + Uvicorn** application using **Jinja2** templates (dependencies managed via Poetry in `pyproject.toml`).
- **Pages & Routes (`ai_art_landing/core/generic.py`)**:
  - `GET /` — Landing page (`core/index.html`); injects monthly return series into `window.chartData` for client-side rendering with Chart.js (`static/dist/js/performance_chart.js`).
  - `GET /about-us.html` — Company, quantitative trading, and HFT overview.
  - `GET /terms-services.html` — Terms of Use.
  - `GET /privacy-policy.html` — Privacy Policy.
  - `GET /favicon.ico` — Site favicon.
- **Templates & Static Assets**:
  - Shared layout (`ai_art_landing/templates/base.html`) and reusable partials (`nav-center.html`, `footer-transparent.html`, `cookies.html`, `script-file.html`).
  - Pre-compiled Tailwind CSS (`ai_art_landing/static/dist/css/tailwind.css`) and third-party UI libraries (`tiny-slider`, `tobii`, `feather-icons`, `@iconscout/unicons`, `@mdi/font` under `ai_art_landing/static/dist/libs/`) are committed directly to the repo.

### Note on `package.json`, `gulpfile.js`, and `tailwind.config.js`

The Node/npm files in the root are leftover build tooling from two merged starter templates:
1. A purchased **Tailwind CSS theme (Techwind)** (`gulpfile.js`, `tailwind.config.js`, and UI library `dependencies` in `package.json`), whose compiled output already lives in `ai_art_landing/static/dist/`.
2. An **LNbits-style FastAPI starter** (`vendor_*` / `bundle` scripts in `package.json` and `vendor.json`), bypassed by default because `bundle_assets = True` in `ai_art_landing/settings.py`.

**Node.js / npm is not needed to run or deploy the website.** You only need npm (`tailwindcss` + `sass`) if you edit `ai_art_landing/static/scss/` or add new Tailwind utility classes not already compiled into `static/dist/css/tailwind.css` (in which case, update `content` in `tailwind.config.js` to `"./ai_art_landing/**/*.{html,js}"`).

## Repository Structure

```text
.
├── ai_art_landing/
│   ├── app.py                  # FastAPI app factory & /static mount
│   ├── server.py               # CLI entrypoint (Uvicorn runner)
│   ├── settings.py             # App configuration & cache-busting static URL helper
│   ├── helpers.py              # Jinja2 environment & CSS/JS asset list loader
│   ├── core/
│   │   ├── generic.py          # Page routes (/, about-us, terms, privacy) & chart data
│   │   └── templates/core/     # Page-specific Jinja2 templates
│   ├── templates/              # Base layout & shared partials (navbar, footer, scripts)
│   └── static/                 # Pre-built CSS/JS/libs (dist/), images, fonts, logos
├── utils/
│   └── logger.py               # Loguru + Uvicorn logging setup
├── Dockerfile                  # Production Python 3.9 + Poetry container image
├── docker-compose.yml          # Local/server container config (maps 8080 -> 5000)
├── deploy.sh                   # Builds, starts detached container & prunes dangling images
└── pyproject.toml              # Python dependencies & `ai_art_landing` CLI script
```

## Running Locally

### Option 1: Poetry (Python 3.8 / 3.9)

```bash
poetry install
poetry run ai_art_landing --host 127.0.0.1 --port 5000 --reload
```

Open `http://127.0.0.1:5000`.

*(If port `5000` is occupied on macOS, e.g. by AirPlay Receiver, pass `--port 8000`.)*

### Option 2: Docker Compose

```bash
./deploy.sh
# or directly:
docker compose up -d --build
```

Open `http://localhost:8080` (maps host port `8080` to container port `5000`).
