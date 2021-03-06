from django.contrib import admin
from .models import Canciones, Album, Artista, Tag, Genero, \
    SubGenero, Instrumento, Banda


class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'banda')


# Register your models here.
admin.site.register(Banda)
admin.site.register(Album)
admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Canciones)
admin.site.register(Genero)
admin.site.register(SubGenero)
admin.site.register(Tag)
admin.site.register(Instrumento)
