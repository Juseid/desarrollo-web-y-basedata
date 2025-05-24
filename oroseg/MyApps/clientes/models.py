from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingrese el nombre del cliente", verbose_name="Nombre del cliente")
    documento = models.CharField(max_length=20, help_text="Ingrese el doumento del cliente")
    telefono = models.CharField(max_length=10, help_text="Ingrese su numero de telefono")
    direccion = models.CharField(max_length=10, help_text="ingrese su direccion")
    correo = models.EmailField(max_length=100, help_text="ingrese su correo")
    

    def __str__(self):
        return self.nombre 

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural="clientes"
    

    