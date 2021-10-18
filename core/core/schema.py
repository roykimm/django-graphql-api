import graphene
from boards.schema import BoardsQuery, BoardCreate, BoardUpdate, BoardDelete


class Query(BoardsQuery):
    pass

class Mutations(graphene.ObjectType):
    board_create = BoardCreate.Field()
    board_delete = BoardDelete.Field()
    board_update = BoardUpdate.Field()

schema = graphene.Schema(
    query=Query,
    mutation=Mutations
)
