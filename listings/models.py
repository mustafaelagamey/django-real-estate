from datetime import datetime

from django.db import models


# Create your models here.
class Listing(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=3, decimal_places=1)
    listing_date = models.DateTimeField(default=datetime.now)
    description = models.TextField()
