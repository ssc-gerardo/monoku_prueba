import graphene
from graphene_django import DjangoObjectType
from .models import Canciones


class CancionesTipos(DjangoObjectType):
    class Meta:
        model = Canciones
        fields = ("id", "nombre", "duracion")


class Query(graphene.ObjectType):

    all_canciones = graphene.List(CancionesTipos)

    def resolve_all_canciones(root, info):
        return Canciones.objects.all()


schema = graphene.Schema(query=Query)
