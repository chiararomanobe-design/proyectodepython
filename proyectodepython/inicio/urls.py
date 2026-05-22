from django.urls import path
from .views import inicio, crear_posteo, registro, eliminar_posteo

urlpatterns = [
    path('',inicio, name="inicio"),
    path("crear/", crear_posteo, name="crear_posteo"),
    path("registro/", registro, name="registro"),
    path("eliminar/<int:posteo_id>/", eliminar_posteo, name="eliminar_posteo"),

]