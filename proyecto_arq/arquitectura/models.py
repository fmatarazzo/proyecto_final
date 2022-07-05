from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Estudios(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    pagina_web = models.URLField(max_length=40)
    email = models.EmailField()
    opinion = models.CharField(max_length=5000 , default = "")

    def __str__(self):
        return f"Nombre: {self.nombre} - Pais: {self.pais} - Pagina web: {self.pagina_web} - Email: {self.email} - Opinion: {self.opinion}"


class Obras(models.Model):
    nombre_obra = models.CharField(max_length=40)
    arquitecto = models.CharField(max_length=40)
    año_construccion = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)
    opinion = models.CharField(max_length=5000, default = "")

    def __str__(self):
        return f"Nombre de obra: {self.nombre_obra} - Arquitecto: {self.arquitecto} - Año construccion: {self.año_construccion} - Ubicacion: {self.ubicacion} - Opinion: {self.opinion}"


class Archviz(models.Model):
    nombre = models.CharField(max_length=40)
    pagina_web = models.URLField(max_length=40)
    email = models.EmailField()
    opinion = models.CharField(max_length=5000 , default = "")

    def __str__(self):
        return f"Nombre: {self.nombre} - Pagina Web: {self.pagina_web} - Email: {self.email} - Opinion: {self.opinion}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank = True)
