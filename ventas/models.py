
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    limite_credito = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=0)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente}"
