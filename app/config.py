from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5433/app"
    redis_url: str = "redis://localhost:6380/0"
    debug: bool = False


settings = Settings()
