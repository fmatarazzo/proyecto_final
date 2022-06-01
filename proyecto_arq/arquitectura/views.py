from django.shortcuts import render
from arquitectura.models import Estudios , Obras
from django.http import HttpResponse
from django.template import loader



# Create your views here.

def inicio(request):
 
    return render(request, "index.html")


def estudios(request):
    estudios = Estudios.objects.all()
    datos = {"datos" : estudios}
    template = loader.get_template("index.html")
    documento = template.render(datos)
    return HttpResponse(documento)
   



def alta_estudios(request):
    estudio = Estudios(nombre="Monoblock" , pais="Argentina" , pagina_web="https://monoblock.cc/" , email="correo@monoblock.cc")
    estudio.save()
    texto = f"Estudio = {estudio.nombre} Pais = {estudio.pais} Pagina Web = {estudio.pagina_web} Contacto = {estudio.email}"
    return HttpResponse(texto)