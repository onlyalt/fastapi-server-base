import uuid

import strawberry
from strawberry.types import Info

from app.graphql.types.car import CarType, CreateCarInput
from app.models.car import Car
from app.services import car as car_service


def _to_graphql(car: Car) -> CarType:
    return CarType(
        id=car.id,
        brand=car.brand,
        model=car.model,
        color=car.color,
        year=car.year,
        description=car.description,
    )


@strawberry.type
class CarQuery:
    @strawberry.field
    async def car(self, info: Info, id: uuid.UUID) -> CarType | None:
        session = info.context["session"]
        car = await car_service.get_car(session, id)
        if car is None:
            return None
        return _to_graphql(car)


@strawberry.type
class CarMutation:
    @strawberry.mutation
    async def create_car(self, info: Info, input: CreateCarInput) -> CarType:
        session = info.context["session"]
        car = await car_service.create_car(
            session,
            brand=input.brand,
            model=input.model,
            color=input.color,
            year=input.year,
            description=input.description,
        )
        return _to_graphql(car)
