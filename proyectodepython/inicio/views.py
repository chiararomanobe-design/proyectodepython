from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Posteo
from .forms import PosteoForm, RegistroForm

def inicio(request):
    posteos = Posteo.objects.all().order_by("-fecha_de_creacion")
    return render(request, 'inicio/inicio.html', {"posteos" : posteos})

@login_required
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

@login_required
def eliminar_posteo(request, posteo_id):
    posteo = get_object_or_404(Posteo, id=posteo_id)

    if posteo.autor == request.user:
        posteo.delete()

    return redirect("inicio")



def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente. Ya puedes iniciar sesion.")
            return redirect("login")
        
    else:
        form = RegistroForm()

    return render(request, "registration/registro.html", {"form": form})

