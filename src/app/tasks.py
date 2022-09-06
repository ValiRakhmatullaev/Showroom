from celery import shared_task
from django.db import transaction
from django.db.models import Q
from celery import shared_task
from django.db import transaction
from django.db.models import Q

from src.app.models import Showroom, ShowroomCar
from src.customer.models import Customer, CustomerOrder
from src.producer.models import ProducerCar, Producer
from src.app.models import Showroom, ShowroomCar
from src.producer.models import ProducerCar, Producer
from src.transaction.models import SalesProducerToShowroom, SalesShowroomToCustomer


@shared_task
def buy_car_from_producer():
    # create QuerySet all showrooms
    for showroom_item in Showroom.objects.all():
        # create query showroom
        query = showroom_item.specification
        # select 2 fields from query instance (dictionary)
        # we can select all fields
        query_brand = query.get("brand")
        query_model = query.get("model")
        query_price = query.get("price")
        # creating QuerySet that matches the showroom's query
        producer_cars = ProducerCar.objects.filter(
            (Q(car__brand__iexact=query_brand) |
             Q(car__model__iexact=query_model)) &
            Q(price__lte=query_price)

        )
        # print(query_brand, query_model, query_price)
        for p_car in producer_cars:
            # select price
            producer_price = p_car.price

            # if DealerSales.objects.filter(car__pk=d_car.car.pk).exists():
            #     item = DealerSales.objects.get(car__pk=d_car.car.pk)
            #     dealer_price = dealer_price - (item.discount * dealer_price)
            #     print(f'dealer_price {dealer_price}')

            # if not cars then scip
            if p_car.count == 0:
                continue

            # if money is not enough
            if showroom_item.balance < producer_price:
                continue

            # # if count of cars = 0
            # if d_car.count <= 0:
            #     continue

            # instances for recording to DB
            showroom_car = ProducerCar.objects.get(pk=p_car.car.pk)
            # showroom_profile = ShowroomProfile.objects.get(pk=showroom_item.pk)
            producer_profile = Producer.objects.get(pk=p_car.producer.pk)

            with transaction.atomic():
                # add car to showroom, increase count
                result = ShowroomCar.objects.update_or_create(
                    car=showroom_car,
                    showroom=showroom_item,
                    producer=producer_profile,
                    price=producer_price,

                )
                # if result == False (item already exist), then increase count +1
                if not result[1]:
                    result[0].count += 1
                    result[0].is_active = True
                    result[0].save()

                # decrease balance in showroom
                showroom_item.balance -= producer_price
                showroom_item.save()

                # increase balance in dealer
                producer_profile.balance += producer_price
                producer_profile.save()

                # decrease car in dealer car
                p_car.count -= 1
                # if cars instance == 0, is active == False
                if p_car.count == 0:
                    p_car.is_active = False
                p_car.save()

                # add transactions
                SalesProducerToShowroom.objects.create(
                    car=showroom_car,
                    showroom=showroom_item,
                    producer=producer_profile,
                    price=producer_price,
                )