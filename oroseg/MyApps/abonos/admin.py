from django.contrib import admin

from MyApps.abonos.models import Abonos

# Register your models here.

class AbonoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Abonos, AbonoAdmin)
