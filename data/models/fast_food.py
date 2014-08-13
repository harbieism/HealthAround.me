from django.contrib.gis.db import models


class FastFood(models.Model):
    '''Data from ReferenceUSA on the location of fast food restaurants.'''

    class Meta:
        verbose_name_plural = "fast-food"
        app_label = "data"

    pnt = models.PointField(srid=4269)
    loader_id = models.IntegerField(default=0)
    objects = models.GeoManager()
