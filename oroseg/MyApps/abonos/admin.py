from django.contrib import admin
from MyApps.abonos.models import Abonos

# Register your models here.

class AbonoAdmin(admin.ModelAdmin):
    list_display = ( 'tipoabono', 'fecha', 'monto')
    # ordering = ('fk_empeño.fk_cliente.nombre', 'tipoabono')  # En caso que sea una sola ordering('column',)
    # #form de busqueda
    # # search_fields = ('Descripcion') #Campo relacionado


admin.site.register(Abonos, AbonoAdmin)
