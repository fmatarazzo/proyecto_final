from django.urls import path
from . import views


urlpatterns = [

    path("" , views.inicio , name="index"),
    #path("alta_estudios" , views.alta_estudios),
    path("estudios" , views.estudios , name="estudios_arquitectura"),
    path("alta_obras_arq" , views.alta_obras_arq),
    path("obras_arq" , views.obras_arq , name="obras_arquitectura"),
    path("contacto" , views.contacto , name="contacto"),
    path("archviz" , views.archviz , name="estudios_archviz"),
    path("alta_estudios" , views.estudios_arq_form)


]