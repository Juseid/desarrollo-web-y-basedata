from django.db import models
from django.utils.timezone import now
from MyApps.empeños.models import Empeños
from MyApps.prendas.models import Prendas


class PrendasPerdidas(models.Model):
    FechaPerdida=models.DateField( verbose_name="Fecha de empeño")
    Fk_empeño = models.OneToOneField(Empeños,
                                  on_delete=models.CASCADE)
    fk_prenda = models.ForeignKey(Prendas,
                              on_delete=models.CASCADE)
    
    def __str__(self):    
        if self.Fk_empeño and self.Fk_empeño.fk_cliente and self.Fk_empeño.fk_cliente.nombre and self.fk_prenda and self.fk_prenda.Descripcion:
            return f"{self.fk_prenda.Descripcion} || {self.Fk_empeño.fk_cliente.nombre}"
        return "Prenda perdida"



    class Meta:
        verbose_name="Prenda Perdida"
        verbose_name_plural="Prendas Perdidas"
