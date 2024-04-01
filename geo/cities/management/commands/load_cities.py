from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import json
from cities.models import City


class Command(BaseCommand):
    '''command that loads cities into database'''

    def handle(self, *args, **options):
        print('start migration')
        json_path = os.path.join(settings.JSON_CITY_DATA)

        count = 0
        with open(json_path) as fl:
            payload = json.load(fl)
            for item in payload:
                City.objects.create(**item)
                count += 1

        print(f'successfully added {count} cities')
