from django.db import models
from MyApps.clientes.models import Clientes
# Create your models here.

class Prendas(models.Model):
    PesoGramos = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="peso de prenda gramos")
    ValorEstimado = models.FloatField(verbose_name="valor estimado")
    Descripcion = models.CharField(max_length=50, verbose_name="descripcion de la joya")
    fk_clientes = models.ForeignKey(Clientes,
                                    null=True,
                                    blank=True,
                                    on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Descripcion


    class Meta:
        verbose_name="prenda"
        verbose_name_plural="prendas"
    