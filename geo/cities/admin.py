from django.contrib import admin
from cities.models import City, GeoLocation

admin.site.register(City, admin.ModelAdmin)
admin.site.register(GeoLocation, admin.ModelAdmin)
