from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import googlemaps
from cities.models import City


class Command(BaseCommand):
	def handle(self, *args, **options):
		key = os.environ.get("MAP_API_KEY")
		gmaps = googlemaps.Client(key=key)
		for city in City.objects.all()[:10]:
			geocode_result = gmaps.geocode(city.search())

			print(geocode_result, '\n')
			sleep(1)

