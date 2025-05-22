from django.contrib import admin

from MyApps.prendas.models import Prendas

# Register your models here.

class PrendasAdmin(admin.ModelAdmin):
    pass


admin.site.register(Prendas, PrendasAdmin)
