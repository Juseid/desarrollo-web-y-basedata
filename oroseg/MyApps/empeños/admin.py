from django.contrib import admin

from MyApps.empeños.models import Empeños

# Register your models here.

class EmpeñosAdmin(admin.ModelAdmin):
    pass


admin.site.register(Empeños, EmpeñosAdmin)
