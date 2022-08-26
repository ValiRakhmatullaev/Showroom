# from core.abstractmodels.date_fields import DateAdded
# from core.filters_models.decimal_range_field import DecimalRangeField
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.db import models
#
#
# class SalesShowroomToCustomer(DateAdded, models.Model):
#     showroom = models.ForeignKey(
#         "showroom.Showroom",
#         on_delete=models.PROTECT,
#         related_name="showroom",
#         null=True,
#     )
#     customer = models.ForeignKey(
#         "customer.Customer",
#         on_delete=models.PROTECT,
#         related_name="customer_transaction_history",
#         null=True,
#     )
#     car = models.ForeignKey(
#         "producer.ProducerCar", on_delete=models.PROTECT, related_name="sold_car", null=True
#     )
#     price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
#     amount_of_discount = models.IntegerField(
#         validators=[MinValueValidator(0), MaxValueValidator(30)]
#     )
#
#     class Meta:
#         db_table = "sales_showroom_to_customer"
#
#     def __str__(self):
#         template = (
#             "{0.showroom} {0.customer} {0.car} {0.price}"
#             " {0.amount_of_discount} {0.added_date}"
#         )
#         return template.format(self)
#
#
# class SalesProducerToShowroom(DateAdded, models.Model):
#     showroom = models.ForeignKey(
#         "showroom.Showroom",
#         on_delete=models.PROTECT,
#         related_name="showroom_that_buys",
#         null=True,
#     )
#     producer = models.ForeignKey(
#         "producer.Producer",
#         on_delete=models.PROTECT,
#         related_name="producer_that_sells",
#         null=True,
#     )
#     car = models.ForeignKey(
#         "producer.ProducerCar", on_delete=models.PROTECT, related_name="car_for_sale", null=True
#     )
#     price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
#     amount_of_discount = models.IntegerField(
#         validators=[MinValueValidator(0), MaxValueValidator(30)]
#     )
#
#     class Meta:
#         db_table = "sales_producer_to_showroom"
#
#     def __str__(self):
#         template = (
#             "{0.showroom} {0.producer} {0.car}"
#             "{0.price} {0.amount_of_discount} {0.added_date}"
#         )
#         return template.format(self)
