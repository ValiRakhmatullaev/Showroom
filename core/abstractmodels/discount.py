from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=100, default="name")
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    amount_of_discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=5
    )
    car = models.ForeignKey(
        "app.ShowroomCar",
        on_delete=models.PROTECT,
        null=True
    )

    class Meta:
        abstract = True


class DiscountRanks:
    """
    - Keys discount percent
    - Values dicosunt representation name
    """
    REGULAR = 0
    BRONZE = 5
    SILVER = 10
    GOLD = 15
    DISCOUNT_CHOICES = [
        (REGULAR, "Regular Client"),
        (BRONZE, "Bronze Client"),
        (SILVER, "Silver Client"),
        (GOLD, "Gold Client"),
    ]
