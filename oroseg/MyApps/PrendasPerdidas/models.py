from django.db import models
from django.utils.timezone import now
from MyApps.empeños.models import Empeños

class PrendasPerdidas(models.Model):
    FechaPerdida=models.DateField(auto_now=True, verbose_name="Fecha de empeño")
    Fk_empeño = models.ForeignKey(Empeños,
                                  null=True,
                                  blank=True,
                                  on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.FechaPerdida


    class Meta:
        verbose_name="PrendasPerdida"
        verbose_name_plural="PrendasPerdidas"
