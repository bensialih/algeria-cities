from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import json
from cities.models import City


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('start migration')
        json_path = os.path.join(settings.BASE_DIR, '../', 'json', 'algeria_cities.json')

        count = 0
        with open(json_path) as fl:
            payload = json.load(fl)
            for item in payload:
                City.objects.create(**item)
                count += 1

        print(f'successfully added {count} cities')

