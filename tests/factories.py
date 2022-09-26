from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, FuzzyDecimal

from src.app.models import Showroom, ShowroomCar
from src.car.models import Car
from src.producer.models import Producer, ProducerCar
from src.users.models import ShowroomUser


class CarFactory(DjangoModelFactory):
    class Meta:
        model = Car

    year = FuzzyInteger(2000, 2022)
    engine = 9


class ShowroomFactory(DjangoModelFactory):
    class Meta:
        model = Showroom


class ProducerFactory(DjangoModelFactory):
    class Meta:
        model = Producer


class ProducerCarFactory(DjangoModelFactory):
    class Meta:
        model = ProducerCar

    car = SubFactory(CarFactory)
    producer = SubFactory(ProducerFactory)
    price = FuzzyDecimal(100)
    count = FuzzyInteger(1)


class ShowroomCarFactory(DjangoModelFactory):
    class Meta:
        model = ShowroomCar

    showroom = SubFactory(ShowroomFactory)
    car = SubFactory(ProducerCarFactory)
    producer = SubFactory(ProducerFactory)
    price = FuzzyDecimal(100)
    count = FuzzyInteger(1)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = ShowroomUser

