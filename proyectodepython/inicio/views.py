from django.shortcuts import render, redirect
from .models import Posteo
from .forms import PosteoForm

def inicio(request):
    posteos = Posteo.objects.all().order_by("-fecha_de_creacion")
    return render(request, 'inicio/inicio.html', {"posteos" : posteos})

def crear_posteo(request):
    if request.method == "POST":
        form = PosteoForm(request.POST)
        
        if form.is_valid():
            posteo = form.save(commit=False)
            posteo.autor = request.user
            posteo.save()
            return redirect("inicio")

    else: 
        form = PosteoForm()

    return render(request, 'inicio/crear_posteo.html', {"form": form})

