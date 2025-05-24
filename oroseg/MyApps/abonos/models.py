from django.db import models
from django.utils.timezone import now
from MyApps.empeños.models import Empeños

# Create your models here.
class Abonos(models.Model):
    estado = [
        ('I','interes'),
        ('C','capital'),   
    ]

    fecha = models.DateField(default=now, verbose_name="Fecha del abono")
    monto= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    tipoabono = models.CharField(max_length=1,choices=estado,default='I')
    fk_empeño=models.ForeignKey (Empeños,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)


    def __str__(self):
        return self.fk_empeño.fk_cliente.nombre

    class Meta:
        verbose_name="abono"
        verbose_name_plural="abonos"



