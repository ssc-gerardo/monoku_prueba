from django.contrib import admin
from .models import Canciones, Album, Artista, Tag, Genero, \
    SubGenero, Instrumento, Banda
# Register your models here.
admin.site.register(Canciones)
admin.site.register(Album)
admin.site.register(Artista)
admin.site.register(Tag)
admin.site.register(Genero)
admin.site.register(SubGenero)
admin.site.register(Instrumento)
admin.site.register(Banda)
