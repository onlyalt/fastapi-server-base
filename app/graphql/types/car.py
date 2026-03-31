import uuid

import strawberry


@strawberry.type
class CarType:
    id: uuid.UUID
    brand: str
    model: str
    color: str
    year: int
    description: str | None


@strawberry.input
class CreateCarInput:
    brand: str
    model: str
    color: str
    year: int
    description: str | None = None
