from django import forms

class EstudiosArq_form(forms.Form):

    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
    pagina_web = forms.URLField(max_length=40)
    email = forms.EmailField()

class ObrasArq_form(forms.Form):

    nombre_obra = forms.CharField(max_length=40)
    arquitecto = forms.CharField(max_length=40)
    año_construccion = forms.DateField
    ubicacion = forms.CharField(max_length=40)
