from django.db import models
from django.utils.timezone import now
from MyApps.clientes.models import Clientes

class PrendasPerdidas(models.Model):
    FechaPerdida=models.DateField(auto_now=True, verbose_name="Fecha de empeño")
    Fk_empeño = models.ForeignKey(Clientes,
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Fk_empeño


    class Meta:
        verbose_name="PrendasPerdida"
        verbose_name_plural="PrendasPerdidas"
