from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class EstudiosArq_form(forms.Form):

    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
    pagina_web = forms.URLField(max_length=40)
    email = forms.EmailField()
    opinion = forms.CharField(max_length=5000)

class ObrasArq_form(forms.Form):

    nombre_obra = forms.CharField(max_length=40)
    arquitecto = forms.CharField(max_length=40)
    año_construccion = forms.CharField(max_length=40)
    ubicacion = forms.CharField(max_length=40)
    opinion = forms.CharField(max_length=5000)

class EstudiosArchviz_form(forms.Form):

    nombre = forms.CharField(max_length=40)
    pagina_web = forms.URLField(max_length=40)
    email = forms.EmailField()
    opinion = forms.CharField(max_length=5000)

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1: forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password1: forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}
