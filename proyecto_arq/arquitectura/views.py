from django.shortcuts import render
from arquitectura.models import Estudios , Obras , Archviz
from django.http import HttpResponse
from django.template import loader



# Create your views here.

def inicio(request):
 
    return render(request, "index.html")


def estudios(request):
    estudios = Estudios.objects.all()
    datos = {"datos" : estudios}
    return render (request , "estudios_arquitectura.html" , datos)

"""
def estudios(request):

    return render(request , "estudios_arquitectura.html")
"""

def contacto(request):
    
    return render (request , "contacto.html")


def alta_estudios(request):
    estudio = Estudios(nombre="Monoblock" , pais="Argentina" , pagina_web="https://monoblock.cc/" , email="correo@monoblock.cc")
    estudio.save()
    texto = f"Estudio = {estudio.nombre} Pais = {estudio.pais} Pagina Web = {estudio.pagina_web} Contacto = {estudio.email}"
    return HttpResponse(texto)



def alta_obras_arq(request):
    obra_arq = Obras(nombre_obra="Norwegian National Opera and Ballet" , arquitecto="Snohetta" , año_construccion="2008-05-05" , ubicacion="Oslo, Noruega")
    obra_arq.save()
    texto = f"Obra = {obra_arq.nombre_obra} Arquitecto = {obra_arq.arquitecto} , Año de construccion = {obra_arq.año_construccion} , Ubicacion = {obra_arq.ubicacion}"
    return HttpResponse(texto)



def obras_arq(request):
    obras_arq = Obras.objects.all
    datos = {"datos" : obras_arq}
    return render (request , "obras_arquitectura.html" , datos)

def archviz(request):
    archviz = Archviz.objects.all
    datos = {"datos" : archviz}
    return render (request , "estudios_archviz.html" , datos)

def estudios_arq_form(request):

    if request.method == "POST":
        estudio = Estudios(nombre=request.POST['nombre'] , pais=request.POST['pais'] , pagina_web=request.POST['pagina web'] , email=request.POST['email'])
        estudio.save()
        return render (request , "estudios_arq_form.html")
    return render (request , "estudios_arq_form.html")