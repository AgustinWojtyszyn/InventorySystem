from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.cantidad})"
    
    def get_absolute_url(self):
        return reverse('detalle_producto', args=[str(self.id)])

class HistorialStock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cantidad_anterior = models.IntegerField()
    cantidad_nueva = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad_anterior} → {self.cantidad_nueva}"
