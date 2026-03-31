# fastapi-server-base

FastAPI + Strawberry GraphQL + PostgreSQL + Redis scaffold.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
make run
```

This starts Postgres and Redis via Docker, runs migrations, and starts the server at `http://localhost:8000`.

GraphQL playground: `http://localhost:8000/graphql`

## Commands

| Command | What it does |
|---|---|
| `make infra` | Start Postgres + Redis containers |
| `make migrate` | Start infra + run Alembic migrations |
| `make run` | Start infra + migrate + start dev server |
