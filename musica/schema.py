import graphene
from graphene_django import DjangoObjectType
from .models import Canciones, Banda, Album, Artista, Tag, \
    Genero, SubGenero, Instrumento


class CancionesTipos(DjangoObjectType):
    class Meta:
        model = Canciones


class BandaTipos(DjangoObjectType):
    class Meta:
        model = Banda


class AlbumTipos(DjangoObjectType):
    class Meta:
        model = Album


class ArtistaTipos(DjangoObjectType):
    class Meta:
        model = Artista


class GeneroTipos(DjangoObjectType):
    class Meta:
        model = Genero


class SubGeneroTipos(DjangoObjectType):
    class Meta:
        model = SubGenero


class TagTipos(DjangoObjectType):
    class Meta:
        model = Tag


class InstrumentoTipos(DjangoObjectType):
    class Meta:
        model = Instrumento


class Query(graphene.ObjectType):

    canciones = graphene.List(CancionesTipos)
    bandas = graphene.List(BandaTipos)
    albums = graphene.List(AlbumTipos)
    artistas = graphene.List(ArtistaTipos)
    generos = graphene.List(GeneroTipos)
    subgeneros = graphene.List(SubGeneroTipos)
    tags = graphene.List(TagTipos)
    instrumentos = graphene.List(InstrumentoTipos)
    canciones_por_genero = graphene.List(
        CancionesTipos, genero=graphene.Int())
    canciones_por_subgenero = graphene.List(
        CancionesTipos, subgenero=graphene.Int())

    def resolve_canciones(root, info):
        return Canciones.objects.all()

    def resolve_bandas(root, info):
        return Banda.objects.all()

    def resolve_albums(root, info):
        return Album.objects.all()

    def resolve_artistas(root, info):
        return Artista.objects.all()

    def resolve_generos(root, info):
        return Genero.objects.all()

    def resolve_subgeneros(root, info):
        return SubGenero.objects.all()

    def resolve_instrumentos(root, info):
        return Instrumento.objects.all()

    def resolve_tags(root, info):
        return Tag.objects.all()

    def resolve_canciones_por_genero(root, info, genero):
        return Canciones.objects.filter(genero=genero)
    
    def resolve_canciones_por_subgenero(root, info, subgenero):
        return Canciones.objects.filter(subgenero=subgenero)


class CreaArtista(graphene.Mutation):
    artista = graphene.Field(ArtistaTipos)

    class Arguments:
        nombre = graphene.String()
        banda_id = graphene.Int()

    def mutate(self, info, nombre, banda_id):
        artista_n = Artista(nombre=nombre)
        banda_n = Banda.objects.get(id=banda_id)
        artista_n.banda = banda_n
        artista_n.save()
        return CreaArtista(artista=artista_n)


class Mutation(graphene.ObjectType):
    creaArtista = CreaArtista.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
