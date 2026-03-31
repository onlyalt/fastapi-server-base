import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.car import Car
from app.repository import car as car_repository


async def get_car(session: AsyncSession, car_id: uuid.UUID) -> Car | None:
    return await car_repository.get_car_by_id(session, car_id)


async def create_car(
    session: AsyncSession,
    *,
    brand: str,
    model: str,
    color: str,
    year: int,
    description: str | None = None,
) -> Car:
    return await car_repository.create_car(
        session,
        brand=brand,
        model=model,
        color=color,
        year=year,
        description=description,
    )
