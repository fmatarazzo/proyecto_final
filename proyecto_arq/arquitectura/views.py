from tkinter import N
from django.shortcuts import render
from arquitectura.models import Estudios , Obras , Archviz , Avatar
from django.http import HttpResponse
from django.template import loader
from arquitectura.forms import EstudiosArq_form , ObrasArq_form , EstudiosArchviz_form , UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required




# Create your views here.


#INICIO

def inicio(request):
    return render(request, "index.html")

def about_me(request):
    return render(request , "about_me.html")

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

@login_required
def alta_estudios(request):

    if request.method == "POST":

        estudio = Estudios(nombre=request.POST['nombre'] , pais=request.POST['pais'] , pagina_web=request.POST['pagina web'] , email=request.POST['email'] , opinion=request.POST['opinion'])
        estudio.save()
        return render (request , "estudios_arq_form.html")
        
        
    return render (request , "estudios_arq_form.html")


#ALTA OBRAS ARQ
@login_required
def alta_obras_arq(request):

    if request.method == "POST":

        obras = Obras(nombre_obra=request.POST['nombre_obra'] , arquitecto=request.POST['arquitecto'] , año_construccion=request.POST['año_construccion'] , ubicacion=request.POST['ubicacion'] , opinion=request.POST['opinion'])
        obras.save()
        return render (request , "obras_arq_form.html")
        
    return render (request , "obras_arq_form.html")


#ALTA ESTUDIOS ARCHVIZ
@login_required
def alta_estudios_archviz(request):

    if request.method == "POST":

        archviz = Archviz(nombre=request.POST['nombre'] , pagina_web=request.POST['pagina_web'] , email=request.POST['email'] , opinion=request.POST['opinion'])
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


#ELIMINAR DATOS DE FORMULARIOS
@login_required
def eliminar_archviz( request , id):
    archviz = Archviz.objects.get(id=id)
    archviz.delete()

    archviz = Archviz.objects.all()

    return render(request , "estudios_archviz.html" , {"datos" : archviz})

@login_required
def eliminar_arq( request , id):
    arq = Estudios.objects.get(id=id)
    arq.delete()

    arq = Estudios.objects.all()

    return render(request , "estudios_arquitectura.html" , {"datos" : arq})


@login_required
def eliminar_obras( request , id):
    obras = Obras.objects.get(id=id)
    obras.delete()

    obras = Obras.objects.all()

    return render(request , "obras_arquitectura.html" , {"datos" : obras})

#EDITAR DATOS DE FORMULARIOS
@login_required
def editar_arq (request , id):

    arq = Estudios.objects.get(id=id)

    if request.method == "POST":
   
              
        mi_formulario = EstudiosArq_form( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            arq.nombre = datos["nombre"]
            arq.pais = datos["pais"]
            arq.pagina_web = datos["pagina_web"]
            arq.email = datos["email"]
            arq.opinion = datos["opinion"]
            arq.save()

            arq = Estudios.objects.all()
            return render(request , "estudios_arquitectura.html" , {"datos": arq})
    else:
        mi_formulario = EstudiosArq_form(initial={"nombre": arq.nombre , "pais": arq.pais , "pagina_web": arq.pagina_web , 'email': arq.email , 'opinion': arq.opinion})


    return render(request , "editar_arq.html" , {"mi_formulario":mi_formulario , "arq": arq})


@login_required
def editar_obras (request , id):

    obras = Obras.objects.get(id=id)

    if request.method == "POST":
   
              
        mi_formulario = ObrasArq_form( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            obras.nombre_obra = datos["nombre_obra"]
            obras.arquitecto = datos["arquitecto"]
            obras.año_construccion = datos["año_construccion"]
            obras.ubicacion = datos["ubicacion"]
            obras.opinion = datos["opinion"]
            obras.save()

            obras = Obras.objects.all()
            return render(request , "obras_arquitectura.html" , {"datos": obras})
    else:
        mi_formulario = ObrasArq_form(initial={"nombre": obras.nombre_obra , "arquitecto": obras.arquitecto , "año_construccion": obras.año_construccion , 'ubicacion': obras.ubicacion , 'opinion': obras.opinion})


    return render(request , "editar_obras.html" , {"mi_formulario":mi_formulario , "obras": obras})


@login_required
def editar_archviz (request , id):

    archviz = Archviz.objects.get(id=id)

    if request.method == "POST":
   
              
        mi_formulario = EstudiosArchviz_form( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            archviz.nombre = datos["nombre"]
            archviz.pagina_web = datos["pagina_web"]
            archviz.email = datos["email"]
            archviz.opinion = datos["opinion"]
            archviz.save()

            archviz = Archviz.objects.all()
            return render(request , "estudios_archviz.html" , {"datos": archviz})
    else:
        mi_formulario = EstudiosArchviz_form(initial={"nombre": archviz.nombre , "pagina_web": archviz.pagina_web , "email": archviz.email , "opinion": archviz.opinion})


    return render(request , "editar_archviz.html" , {"mi_formulario":mi_formulario , "archviz": archviz})


#LOGIN

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request , "index.html" , {"url":avatares[0].imagen.url})

            else:
                return render(request , "index.html" , {"mensaje": "Error, datos incorrectos"}) 
            
        else:
            return render(request , "index.html" , {"mensaje":"Formulario erroneo"})
    
    form = AuthenticationForm()

    return render(request, "login.html" , {"form":form})


def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render (request , "usuario_creado.html")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})


@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":

        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render(request , "inicio.html")

    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email})

    return render (request , "editar_perfil.html" , {"mi_formulario":mi_formulario , "usuario":usuario})
