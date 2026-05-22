from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Posteo


class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ["titulo", "contenido"]

class RegistroForm(UserCreationForm):
    pass

class PerfilForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ["first_name", "last_name", "email"]