from celery import shared_task
from django.db import transaction
from django.db.models import Q

from src.app.models import Showroom, ShowroomCar
from src.customer.models import Customer, CustomerOrder
from src.producer.models import ProducerCar, Producer
from src.transaction.models import SalesShowroomToCustomer


@shared_task
def buy_car_from_showroom():
    # create QuerySet all customer
    for customer_item in Customer.objects.all():
        query = customer_item.specification
        query_brand = query.get("brand")
        query_model = query.get("model")
        query_price = query.get("price")

        showroom_cars = ShowroomCar.objects.filter(
            (Q(car__car__brand__iexact=query_brand) |
             Q(car__car__model__iexact=query_model)) &
            Q(price__lte=query_price)
        )
        for sh_car in showroom_cars:
            # select price
            showroom_price = sh_car.price

            if sh_car.count == 0:
                continue

            # if money is not enough
            if customer_item.balance < showroom_price:
                continue

            # instances for recording to DB
            customer_car = ShowroomCar.objects.get(car=sh_car.car)
            # showroom_profile = ShowroomProfile.objects.get(pk=showroom_item.pk)
            showroom_profile = Showroom.objects.get(pk=sh_car.showroom.pk)
            with transaction.atomic():
                # add car to showroom, increase count
                result = CustomerOrder.objects.update_or_create(
                    car=customer_car,
                    customer=customer_item,
                    showroom=showroom_profile,
                    price=showroom_price,
                )
                # if result == False (item already exist), then increase count +1
                if not result[1]:
                    # result[0].count += 1
                    result[0].is_active = True
                    result[0].save()

                # decrease balance in customer
                customer_item.balance -= showroom_price
                customer_item.save()

                # increase balance in showroom
                showroom_profile.balance += showroom_price
                showroom_profile.save()

                # decrease car in customer car
                sh_car.count -= 1
                # if cars instance == 0, is active == False
                if sh_car.count == 0:
                    sh_car.is_active = False
                sh_car.save()

                # add transactions
                SalesShowroomToCustomer.objects.create(
                    car=customer_car,
                    customer=customer_item,
                    showroom=showroom_profile,
                    price=showroom_price,
                )
