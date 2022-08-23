from django.db import models
from django_countries.fields import CountryField

from core.filters.decimal_range_field import DecimalRangeField


class Information(models.Model):
    name = models.CharField(max_length=100)
    balance = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00, default=0.00)
    country = CountryField(multiple=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    class Meta:
        abstract = True
