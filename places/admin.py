from django.conf import settings
from django.contrib import admin

from places.models import Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ( 'latitude', 'longitude','radius',)

    fieldsets = (
        (None, {
            'fields': ('latitude', 'longitude','radius')
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('/static/style.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                '/static/places.js',
            )