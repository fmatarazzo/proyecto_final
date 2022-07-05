from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path("" , views.inicio , name="index"),
    path("about_me" , views.about_me , name="about_me"),
    path("estudios" , views.estudios , name="estudios_arquitectura"),
    path("alta_obras_arq" , views.alta_obras_arq , name ="obras_arq_form"),
    path("obras_arq" , views.obras_arq , name="obras_arquitectura"),
    path("contacto" , views.contacto , name="contacto"),
    path("archviz" , views.archviz , name="estudios_archviz"),
    path("alta_estudios" , views.alta_estudios , name="estudios_arq_form"),
    path("buscar" , views.buscar , name="buscar_info"),
    path("resultado_busqueda" , views.resultado_busqueda , name="resultado_busqueda"),
    path("alta_estudios_archviz" , views.alta_estudios_archviz , name="estudios_archviz_form"),
    path("eliminar_archviz/<int:id>" , views.eliminar_archviz , name="eliminar_archviz"),
    path("eliminar_arq/<int:id>" , views.eliminar_arq , name="eliminar_arq"),
    path("eliminar_obras/<int:id>" , views.eliminar_obras , name="eliminar_obras"),
    path("editar_arq/<int:id>" , views.editar_arq , name="editar_arq"),
    path("editar_arq" , views.editar_arq , name="editar_arq"),
    path("editar_obras/<int:id>" , views.editar_obras , name="editar_obras"),
    path("editar_obras" , views.editar_obras , name="editar_obras"),
    path("editar_archviz/<int:id>" , views.editar_archviz , name="editar_archviz"),
    path("editar_archviz" , views.editar_archviz , name="editar_archviz"),
    path("login" , views.login_request , name="login"),
    path("register" , views.register , name="register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="logout"),
    path("editar_perfil" , views.editar_perfil , name="editar_perfil")            
    


]