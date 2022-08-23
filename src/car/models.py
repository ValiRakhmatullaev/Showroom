from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime

from core.abstractmodels.date_fields import DateUpdatedAdded
from core.enum.enums import CarType


class Car(DateUpdatedAdded):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2022)])
    engine = models.PositiveIntegerField(validators=[MinValueValidator(0.5), MaxValueValidator(9)])
    body_type = models.CharField(max_length=100, choices=CarType.choices(), default=True)
    image = models.URLField(blank=True, max_length=100)

    def __str__(self):
        template = (
            "{0.brand} {0.model} {0.color} {0.year} {0.engine}"
            "{0.body_type}"
        )
        return template.format(self)

    class Meta:
        db_table = "car"
