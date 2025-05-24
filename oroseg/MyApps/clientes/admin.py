from django.contrib import admin

from MyApps.clientes.models import Clientes

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'documento', 'telefono', 'correo')
    ordering = ('nombre', 'documento', 'telefono', 'correo')  # En caso que sea una sola ordering('column',)
    #form de busqueda
    search_fields = ('nombre','correo') #Campo relacionado

    list_filter = ('nombre', 'correo','documento') # Campos relacionados



admin.site.register(Clientes, ClienteAdmin)
