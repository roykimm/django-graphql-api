import graphene
from graphene_django.types import DjangoObjectType
from .models import Boards


class BoardsType(DjangoObjectType):
    class Meta:
        model = Boards


class BoardsQuery(graphene.ObjectType):
    allBoards = graphene.List(BoardsType)

    def resolve_allBoards(root, info, **kwargs):
        return Boards.objects.all()
