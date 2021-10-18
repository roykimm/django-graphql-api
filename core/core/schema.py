import graphene
from boards.schema import BoardsQuery


class Query(
    BoardsQuery,
):
    pass


schema = graphene.Schema(query=Query)
