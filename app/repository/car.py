import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.car import Car


async def get_car_by_id(session: AsyncSession, car_id: uuid.UUID) -> Car | None:
    result = await session.execute(select(Car).where(Car.id == car_id))
    return result.scalar_one_or_none()


async def create_car(
    session: AsyncSession,
    *,
    brand: str,
    model: str,
    color: str,
    year: int,
    description: str | None = None,
) -> Car:
    car = Car(brand=brand, model=model, color=color, year=year, description=description)
    session.add(car)
    await session.commit()
    await session.refresh(car)
    return car
