from django.db import models
from bases.models import ClaseModelo

# Create your models here.
class Proveedor(ClaseModelo):
    descripcion = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return f'{self.descripcion}'
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()
    class Meta:
        verbose_name_plural = "Proveedores"
