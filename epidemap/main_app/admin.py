from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin
from .consts import ModelConstants


# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    #list_display = (ModelConstants.Incidences.DB_COL_NAME, ModelConstants.Incidences.DB_COL_LOCATION)
    default_zoom = 2

admin.site.register(Incidences, IncidencesAdmin)    
