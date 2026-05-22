from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Posteo(models.Model):
    titulo=models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_de_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo