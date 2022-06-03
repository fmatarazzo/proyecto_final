from django.shortcuts import render
from arquitectura.models import Estudios , Obras , Archviz
from django.http import HttpResponse
from django.template import loader
from arquitectura.forms import EstudiosArq_form , ObrasArq_form



# Create your views here.


#INICIO

def inicio(request):
 
    return render(request, "index.html")

#PAGINA PRINCIPAL ESTUDIOS ARQUITECTURA

def estudios(request):
    estudios = Estudios.objects.all()
    datos = {"datos" : estudios}
    return render (request , "estudios_arquitectura.html" , datos)

#PAGINA PRINCIPAL CONTACTO

def contacto(request):
    
    return render (request , "contacto.html")


#PAGINA PRINCIPAL OBRAS ARQ

def obras_arq(request):
    obras_arq = Obras.objects.all
    datos = {"datos" : obras_arq}
    return render (request , "obras_arquitectura.html" , datos)

#PAGINA PRINCIPAL ESTUDIOS ARCHVIZ

def archviz(request):
    archviz = Archviz.objects.all
    datos = {"datos" : archviz}
    return render (request , "estudios_archviz.html" , datos)

#ALTA ESTUDIOS ARQ


def alta_estudios(request):

    if request.method == "POST":

        estudio = Estudios(nombre=request.POST['nombre'] , pais=request.POST['pais'] , pagina_web=request.POST['pagina web'] , email=request.POST['email'])
        estudio.save()
        return render (request , "estudios_arq_form.html")
        
    return render (request , "estudios_arq_form.html")


#ALTA OBRAS ARQ

def alta_obras_arq(request):

    if request.method == "POST":

        obras = Obras(nombre_obra=request.POST['nombre_obra'] , arquitecto=request.POST['arquitecto'] , año_construccion=request.POST['año_construccion'] , ubicacion=request.POST['ubicacion'])
        obras.save()
        return render (request , "obras_arq_form.html")
        
    return render (request , "obras_arq_form.html")


#ALTA ESTUDIOS ARCHVIZ

def alta_estudios_archviz(request):

    if request.method == "POST":

        archviz = Archviz(nombre=request.POST['nombre'] , pagina_web=request.POST['pagina_web'] , email=request.POST['email'])
        archviz.save()
        return render (request , "estudios_archviz_form.html")
        
    return render (request , "estudios_archviz_form.html")


#BUSCAR ESTUDIO ARQ

def buscar(request):

    return render( request , "buscar_info.html")

def resultado_busqueda(request):

    if request.GET['nombre']:
        nombre= request.GET['nombre']
        estudios= Estudios.objects.filter(nombre__icontains=nombre)
        return render(request , "resultado_busqueda.html" ,  {"estudios" : estudios})
    else:
        return HttpResponse("Campo vacio")

    
