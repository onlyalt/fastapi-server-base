import strawberry

from app.graphql.resolvers.car import CarMutation, CarQuery


@strawberry.type
class Query(CarQuery):
    pass


@strawberry.type
class Mutation(CarMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
