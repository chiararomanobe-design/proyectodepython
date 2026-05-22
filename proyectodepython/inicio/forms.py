from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Posteo


class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ["titulo", "contenido"]

class RegistroForm(UserCreationForm):
    pass