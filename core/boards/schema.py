import graphene
from graphene_django.types import DjangoObjectType
from .models import Boards


class BoardsType(DjangoObjectType):
    class Meta:
        model = Boards
        fields = ('b_no', 'b_title','b_note','b_writer','b_count','b_date')


class BoardsQuery(graphene.ObjectType):
    Boards_all = graphene.List(BoardsType)
    Boards_detail = graphene.Field(BoardsType, b_no=graphene.Int(required=True))

    def resolve_Boards_all(root, info, **kwargs):
        return Boards.objects.filter(usage_flag='1')

    def resolve_Boards_detail(self, info, b_no):
        return Boards.objects.get(b_no=b_no)


class BoardCreate(graphene.Mutation):

    class Arguments:
        bTitle = graphene.String()
        bWriter = graphene.String()
        bNote = graphene.String()

    boards = graphene.Field(BoardsType)

    def mutate(self, info, bTitle, bWriter, bNote):
        boards = Boards.objects.create(b_title=bTitle, b_writer=bWriter, b_note=bNote)

        return BoardCreate(boards=boards)

class BoardDelete(graphene.Mutation):

    class Arguments:
        bNo = graphene.Int()

    boards = graphene.Field(BoardsType)

    def mutate(self, info, bNo):
        boards = Boards.objects.get(b_no=bNo)
        boards.usage_flag = '0'
        boards.save()
        return BoardDelete(boards=boards)

class BoardUpdate(graphene.Mutation):

    class Arguments:
        bNo = graphene.Int()
        bTitle = graphene.String()
        bWriter = graphene.String()
        bNote = graphene.String()

    boards = graphene.Field(BoardsType)

    def mutate(Self,info,bNo, bTitle, bWriter, bNote):

        boards = Boards.object.get(b_no=bNo)
        boards.b_title = bTitle
        boards.b_writer = bWriter
        boards.b_note = bNote
        boards.save()
        return BoardUpdate(boards = boards)
    

