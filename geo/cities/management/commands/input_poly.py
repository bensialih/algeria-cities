from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
import json
from cities.models import City


class Command(BaseCommand):
    '''command that loads cities into database'''

    def handle(self, *args, **options):
        '''
            todo: create a command that will take 
            id: "[ list of co-ord here ]" and insert 
            them into cities.Geolocation model.

            there are 1049 commutes.
            if I draw out 20 per day, I should be done in 52 days
            this tool is just to make it easier.
        '''
        pass
