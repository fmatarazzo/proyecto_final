from django.urls import path
from . import views


urlpatterns = [

    path("" , views.inicio , name="index"),
    path("estudios" , views.estudios , name="estudios_arquitectura"),
    path("alta_obras_arq" , views.alta_obras_arq , name ="obras_arq_form"),
    path("obras_arq" , views.obras_arq , name="obras_arquitectura"),
    path("contacto" , views.contacto , name="contacto"),
    path("archviz" , views.archviz , name="estudios_archviz"),
    path("alta_estudios" , views.alta_estudios , name="estudios_arq_form"),
    path("buscar" , views.buscar , name="buscar_info"),
    path("resultado_busqueda" , views.resultado_busqueda , name="resultado_busqueda"),
    path("alta_estudios_archviz" , views.alta_estudios_archviz , name="estudios_archviz_form")
    


]