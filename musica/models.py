from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class SubGenero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Banda(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nombre


class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Albums"


class Artista(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Canciones(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True)
    subgenero = models.ForeignKey(
        SubGenero, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    duracion = models.TimeField(blank=True)
    fecha = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Instrumento(models.Model):
    cancion = models.ForeignKey(
        Canciones, related_name='instrumentos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Tag(models.Model):
    cancion = models.ForeignKey(
        Canciones, related_name='tags', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
