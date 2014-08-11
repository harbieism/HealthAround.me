from django.core.management.base import BaseCommand
from data.fast_food.loading import fast_food_importer

import logging


class Command(BaseCommand):
    args = ''
    help = 'Import Fast Food data'

    def handle(self, *args, **options):
        logging.basicConfig(
            level=logging.INFO,
            format=" %(levelname)s %(name)s: %(message)s")
        fast_food_importer()
