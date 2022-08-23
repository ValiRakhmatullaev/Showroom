from django.db import models

from core.abstractmodels.common_info import Information
from core.abstractmodels.date_fields import DateAddedUpdated
from core.abstractmodels.discount import Discount
from core.filters.decimal_range_field import DecimalRangeField


class Showroom(DateAddedUpdated, Information):
    specification = models.JSONField(
        encoder=None,
        decoder=None,
        default={
            "auto_name": "chevrolet",
            "model": "malibu",
            "color": "blue",
            "year": "2017",
            "price": 10000,
            "engine": 1.5,
            "body_type": "sedan",
        },
    )

    def __str__(self):
        template = "{0.name} {0.country} {0.email}"
        return template.format(self)

    class Meta:
        db_table = "app"


class  ShowroomCar(models.Model):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    car = models.ForeignKey("producer.ProducerCar", on_delete=models.CASCADE)
    producer = models.ForeignKey("producer.Producer", on_delete=models.CASCADE)
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        template = "{0.car} {0.price} {0.count}"
        return template.format(self)


class DiscountShowroom(DateAddedUpdated, Discount):
    showrooms_discount = models.ForeignKey(
        "Showroom",
        on_delete=models.PROTECT,
        related_name="discount",
        null=True,
    )

    class Meta:
        db_table = "showroom_discount"

    def __str__(self):
        template = (
            "{0.name}"
            "{0.amount_of_discount}"
        )
        return template.format(self)
