from django.contrib import admin

from MyApps.PrendasPerdidas.models import PrendasPerdidas

# Register your models here.

class PrendasPerdidasAdmin(admin.ModelAdmin):
    list_display = ("Fk_empeño",'fk_prenda','FechaPerdida',)



admin.site.register(PrendasPerdidas, PrendasPerdidasAdmin)
