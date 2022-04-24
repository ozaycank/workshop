from django.db import models

#Area model create attributes.

class Area(models.Model):                                 
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)     #Longtitude field
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)      #Latitude field
    radius = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)        #Radius field
