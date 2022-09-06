from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.abstractmodels.common_info import Information
from core.abstractmodels.date_fields import DateUpdatedAdded, DateAddedUpdated
from core.filters.decimal_range_field import DecimalRangeField


class Customer(DateUpdatedAdded, Information):
    age = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(150)])
    driver_licence = models.BooleanField(default=True)
    specification = models.JSONField(
        default={
            "brand": "",
            "model": "",
            "color": "",
            "year": "",
            "engine": "",
            "price": "",
            "body_type": "",
        },
    )

    class Meta:
        db_table = "customer"

    def __str__(self):
        template = "{0.name} {0.age} {0.country} {0.email}"
        return template.format(self)


class CustomerOrder(DateAddedUpdated):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="customer_orders", null=True)
    showroom = models.ForeignKey("app.Showroom", on_delete=models.PROTECT, related_name="showroom_cars", null=True)
    car = models.ForeignKey("app.ShowroomCar", on_delete=models.PROTECT, related_name="showroom_car", null=True)
    price = models.ForeignKey("app.ShowroomCar", on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = "customer_order"

    def __str__(self):
        template = "{0.customer} {0.car} {0.price}"
        return template.format(self)
