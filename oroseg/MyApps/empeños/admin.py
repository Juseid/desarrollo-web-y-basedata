from django.contrib import admin

from MyApps.empeños.models import Empeños

# Register your models here.

class EmpeñosAdmin(admin.ModelAdmin):
    list_display = ( 'FechaEmpeño', 'PlazoMeses', 'InteresMensual','Estado')
    # ordering = ('fk_empeño.fk_cliente.nombre', 'tipoabono')  # En caso que sea una sola ordering('column',)
    # #form de busqueda
    # # search_fields = ('Descripcion') #Campo relacionado


admin.site.register(Empeños, EmpeñosAdmin)
