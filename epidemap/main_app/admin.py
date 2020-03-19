from django.contrib import admin
from .models import *
from .consts import ModelConstants

# Register your models here.

class IncidencesAdmin(admin.ModelAdmin):
    list_display = (ModelConstants.Incidences.DB_COL_NAME, ModelConstants.Incidences.DB_COL_LOCATION)

admin.site.register(Incidences, IncidencesAdmin)    
