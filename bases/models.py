from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now_add=True)
    usuarioCreador = models.ForeignKey(User, on_delete=models.CASCADE)
    usuarioModificador = models.IntegerField(blank=True, null=True)
    class Meta:
        abstract = True
