from celery import shared_task
from celery.utils.log import get_task_logger

# from producer.models import Car, DiscountDealer, LoyaltyProgram
# from django.db import transaction
# from django.db.models import Q
# from app.models import Showroom
# from transaction.models import SalesDealerToShowroom

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")


# @shared_task
# def showroom_buy_cars():
#     """
#     :param app: Showroom model Instance
#     :param showroom_preference: Showroom preferences
#     :param car_dealer_search: Complex filter for finding cars at the producer
#     :param dealer_cars: Filtered cars
#     :param dealer_car: Dealers model car instance
#     """
#     for app in Showroom.objects.all():
#         showroom_preference = app.specification
#
#         car_dealer_search = (
#             Q(car__make__startswith=showroom_preference.get("make"))
#             & Q(car__model__icontains=showroom_preference.get("model"))
#             & Q(car__color__icontains=showroom_preference.get("color"))
#             & Q(car__year__exact=showroom_preference.get("year"))
#             & Q(car__engine__exact=showroom_preference.get("engine"))
#             & Q(car__body_type__icontains=showroom_preference.get("body_type"))
#         )
#
#         dealer_cars = Car.objects.filter(
#             car_dealer_search, showroom__isnull=True, customer__isnull=True
#         ).order_by("price")
#         for dealer_car in dealer_cars:
#             with transaction.atomic():
#                 discount_dealer, created = DiscountDealer.objects.get_or_create(
#                     app=app, producer=dealer_car.producer
#                 )
#                 price = dealer_car.price * ((100 - discount_dealer.discount) / 100)
#                 if app.balance - price > 0:
#                     SalesDealerToShowroom.objects.create(
#                         app=app,
#                         producer=dealer_car.producer,
#                         car=dealer_car,
#                         price=price,
#                     )
#                     dealer_car.app = app
#                     dealer_car.price += 100
#                     dealer_car.save(update_fields=["app", "price"])
#                     app.balance -= price
#                     app.save(update_fields=["balance"])
#                     discount_dealer.bought_cars += 1
#                     discount_dealer.save(update_fields=["bought_cars"])
#                     loyality_program = (
#                         LoyaltyProgram.objects.filter(
#                             producer=dealer_car.producer,
#                             min_bought_cars__lte=discount_dealer.bought_cars,
#                         )
#                         .order_by("-min_bought_cars")
#                         .first()
#                     )
#                     if (
#                         loyality_program
#                         and loyality_program.program != discount_dealer.discount
#                     ):
#                         discount_dealer.discount = loyality_program.program
#                         discount_dealer.save(update_fields=["discount"])
