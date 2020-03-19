from django.db import models
from .consts import ModelConstants

# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=200, db_column = ModelConstants.Incidences.DB_COL_NAME)
    location = models.CharField(max_length=20, db_column = ModelConstants.Incidences.DB_COL_LOCATION)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"