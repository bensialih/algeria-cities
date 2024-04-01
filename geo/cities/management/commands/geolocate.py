from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import googlemaps
from cities.models import City
import time


class Command(BaseCommand):
	def handle(self, *args, **options):
		'''API request to get geolocation of cities'''

		key = os.environ.get("MAP_API_KEY")
		gmaps = googlemaps.Client(key=key)
		for city in City.objects.all()[:10]:
			geocode_result = gmaps.geocode(city.search())

			print(geocode_result, '\n')
			time.sleep(1)
