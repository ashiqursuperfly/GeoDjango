from django.db import models
from django.contrib.gis.db import models as geomodels
from .consts import ModelConstants

# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=200)
    location = geomodels.PointField(srid=4326)
    objects = geomodels.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"