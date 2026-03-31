.PHONY: run infra migrate

infra:
	@echo "Starting PostgreSQL and Redis..."
	@docker compose up -d db redis
	@echo "Waiting for services to be healthy..."
	@until docker compose exec db pg_isready -U postgres > /dev/null 2>&1; do sleep 1; done
	@until docker compose exec redis redis-cli ping > /dev/null 2>&1; do sleep 1; done
	@echo "Infrastructure is ready."

migrate: infra
	@echo "Running pending migrations..."
	@.venv/bin/alembic upgrade head
	@echo "Migrations are up to date."

run: migrate
	@echo "Starting server with hot reload..."
	@.venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
