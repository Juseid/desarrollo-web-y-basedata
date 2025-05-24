from django.contrib import admin

from MyApps.prendas.models import Prendas

# Register your models here.

class PrendasAdmin(admin.ModelAdmin):
    # preadonly_fields = ('correoCliente',) #No permite edicion de create y update
    # readonly_fields = ('created', 'updated') #No permite edicion de create y update
    list_display = ('Descripcion', 'ValorEstimado', 'PesoGramos')
    # ordering = ('Descripcion', 'ValorEstimado', 'PesoGramos')  # En caso que sea una sola ordering('column',)
    # #form de busqueda
    # # search_fields = ('Descripcion') #Campo relacionado

    # list_filter = ('Descripcion', 'ValorEstimado','PesoGramos') # Campos relacionados



admin.site.register(Prendas, PrendasAdmin)
