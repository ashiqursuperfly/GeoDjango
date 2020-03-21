from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin
from .consts import ModelConstants

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    list_display = (ModelConstants.Incidences.DB_COL_NAME, ModelConstants.Incidences.DB_COL_LOCATION)

class BdUnionsAdmin(LeafletGeoAdmin):
    list_display = (ModelConstants.BdUnions.DB_COL_DISTRICT_NAME, ModelConstants.BdUnions.DB_COL_UNION_NAME)

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(BdUnions, BdUnionsAdmin)
