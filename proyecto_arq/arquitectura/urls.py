from django.urls import path
from . import views


urlpatterns = [

    path("inicio" , views.inicio),
    path("alta_estudios" , views.alta_estudios),
    path("estudios" , views.estudios)

]