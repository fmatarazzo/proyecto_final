from django.db import models

# Create your models here.


class Estudios(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    pagina_web = models.URLField(max_length=40)
    email = models.EmailField()

class Obras(models.Model):
    nombre_obra = models.CharField(max_length=40)
    arquitecto = models.CharField(max_length=40)
    año_construccion = models.DateField()
    ubicacion = models.CharField(max_length=40)

class Archviz(models.Model):
    nombre = models.CharField(max_length=40)
    pagina_web = models.URLField(max_length=40)
    email = models.EmailField()