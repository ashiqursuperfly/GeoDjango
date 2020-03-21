from django.contrib.gis.db import models
from .consts import ModelConstants

# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=200, db_column=ModelConstants.Incidences.DB_COL_NAME)
    location = models.PointField(srid=4326, db_column=ModelConstants.Incidences.DB_COL_LOCATION)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"


class BdUnions(models.Model):
    div_id = models.CharField(max_length=254)
    dist_id = models.CharField(max_length=254)
    upz_id = models.CharField(max_length=254)
    un_id = models.CharField(max_length=254)
    un_uid = models.CharField(max_length=254)
    divi_name = models.CharField(max_length=254)
    dist_name = models.CharField(max_length=254)
    upaz_name = models.CharField(max_length=254)
    uni_name = models.CharField(max_length=254)
    area_sqkm = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.uni_name + ":" + self.dist_name

    class Meta:
        verbose_name_plural = "BDUnions"  