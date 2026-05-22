from django.shortcuts import render
from .models import Posteo

def inicio(request):
    posteos = Posteo.objects.all().order_by("-fecha_de_creacion")
    return render(request, 'inicio/inicio.html', {"posteos" : posteos})

