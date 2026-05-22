from django.urls import path
from .views import inicio, crear_posteo

urlpatterns = [
    path('',inicio, name="inicio"),
    path("crear/", crear_posteo, name="crear_posteo")
]