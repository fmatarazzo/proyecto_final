from django.urls import path
from . import views


urlpatterns = [

    path("inicio" , views.inicio),
    path("alta_estudios" , views.alta_estudios),
    path("estudios" , views.estudios),
    path("alta_obras_arq" , views.alta_obras_arq),
    path("obras_arq" , views.obras_arq)

]