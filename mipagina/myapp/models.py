from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tareas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.usuario.username}"
    
    