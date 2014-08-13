import csv
import logging

from django.contrib.gis.geos import Point
from data.models import FastFood

logger = logging.getLogger(__name__)


def fast_food_importer():
    fast_food_db_importer()


def fast_food_db_importer():
    path = 'data/fast_food/fast_food_lat_lon_ok.csv'
    reader = csv.reader(file(path))
    count = 1
    for lat, lng in reader:
        float_lat = float(lat)
        float_lng = float(lng)
        new_pnt = Point(float_lng, float_lat)
        new_fast_food_location, created = FastFood.objects.get_or_create(
            pnt=new_pnt,
            loader_id=count
        )
        new_fast_food_location.save()
        count += 1
        print count
    logger.info("Imported {} fast food locations".format(count))
