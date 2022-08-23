from django.db import models

from core.abstractmodels.common_info import Information
from core.abstractmodels.date_fields import DateAddedUpdated
from core.abstractmodels.discount import DiscountRanks, Discount
from core.filters.decimal_range_field import DecimalRangeField


class Producer(DateAddedUpdated, Information):
    found_year = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    number_of_buyers = models.PositiveIntegerField(default=0)
    cars = models.ManyToManyField("car.Car", through="ProducerCar")

    class Meta:
        db_table = "producer"

    def __str__(self):
        template = "{0.id} {0.name}"
        return template.format(self)


class ProducerCar(models.Model):
    car = models.ForeignKey("car.Car", related_name="producer_car", on_delete=models.PROTECT)
    producer = models.ForeignKey("producer.Producer", on_delete=models.PROTECT)
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
    count = models.PositiveIntegerField(default=0)
    is_sale = models.BooleanField(default=False)


class DiscountProducer(DateAddedUpdated, Discount):
    """
    Discounts Producer - ShowRoom
    """
    discount = models.IntegerField(
        choices=DiscountRanks.DISCOUNT_CHOICES,
        default=DiscountRanks.REGULAR
    )
    bought_cars = models.PositiveIntegerField(default=0)
    producer = models.ForeignKey(
        Producer,
        related_name="discounts",
        on_delete=models.PROTECT,
        null=True
    )

    class Meta:
        db_table = "producer_discount"

    def __str__(self):
        template = "{0.discount} {0.bought_cars}" "{0.producer}"
        return template.format(self)


class LoyaltyProgram(DateAddedUpdated):
    """
    Loyalty program is unique for every producer
    and discount by number of bought cars
    is different.

    min_bought_cars: minimum value for achieve this particular program.

    DealerDiscount.discount updates depends on LoyaltyProgram
    """

    producer = models.ForeignKey(Producer, related_name="producer_loyalties", on_delete=models.CASCADE)
    program = models.IntegerField(choices=DiscountRanks.DISCOUNT_CHOICES, default=DiscountRanks.REGULAR)
    min_bought_cars = models.PositiveIntegerField()

    def __str__(self):
        if self.producer:
            return f"{self.producer} - {self.program}"
        return "New Loyalty Program"
