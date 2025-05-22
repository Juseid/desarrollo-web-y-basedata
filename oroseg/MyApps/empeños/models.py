from django.db import models
from MyApps.clientes.models import Clientes


# Create your models here.

class Empeños(models.Model):
    estado = [
        ("A","activo"),
        ("R", "recuperado"),
        ("P", "perdido"),
    ]
    FechaEmpeño = models.DateField(auto_now=True, verbose_name="Fecha de Empeño")
    PlazoMeses = models.IntegerField(default=4, editable=False, verbose_name="Plazo mes")
    InteresMensual = models.DecimalField(max_digits=10,decimal_places=2, verbose_name="interes por MES")
    Estado = models.CharField(max_length=1,choices=estado, default="A", verbose_name="estado del empeño")
    fk_cliente = models.ForeignKey(Clientes,
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.Estado

    class Meta:
        verbose_name="empeño"
        verbose_name_plural="empeños"