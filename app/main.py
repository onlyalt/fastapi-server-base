from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.persistence.db import async_session, engine
from app.graphql.schema import schema
from app.persistence.redis import redis_client


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None]:
    yield
    await engine.dispose()
    await redis_client.aclose()


async def get_context():
    async with async_session() as session:
        yield {"session": session}


graphql_app: GraphQLRouter = GraphQLRouter(schema, context_getter=get_context)  # type: ignore[type-arg]

app = FastAPI(title="Fast Server Base", lifespan=lifespan)
app.include_router(graphql_app, prefix="/graphql")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
