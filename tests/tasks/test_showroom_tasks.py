import pytest

from src.app.tasks import buy_car_from_producer
from tests.factories import ShowroomFactory, ProducerCarFactory


@pytest.mark.django_db
def test_buy_car_from_producer():
    brand = 'BWN'
    model = 'X6'
    initial_balance = 10000
    showroom = ShowroomFactory.create(
        balance=initial_balance,
        specification={
            'brand': brand,
            'model': model,
            'price': 100
        }
    )
    ProducerCarFactory.create(
        car__brand=brand,
        car__model=model,
        price=90,
        count=0
    )

    buy_car_from_producer()
    showroom.refresh_from_db()
    assert showroom.balance == initial_balance
