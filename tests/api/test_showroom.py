import pytest
#
# from src.customer.models import Customer
#
# url = "/api/customer/list/"
# detail_url = "/api/customer/1/details/"
#
# payload = dict(
#     name="John",
#     balance="John",
#     country="UK",
#     email="J@ufc.com",
#     password="ufcufc",
# )
# update_payload = dict(
#     name="Leo",
#     balance="Lionel",
#     country="UZ",
#     email="L@ufc.com",
#     password="LionelM",
# )
#
#
# @pytest.mark.django_db
# def test_customer_get(client, auth_client, get_responses):
#     """
#     Ensure that anybody can get a list of Customers.
#     Ensure that only authenticated users can get a detail list of Customers.
#     """
#     assert get_responses(client=client, url=url) == 200
#     assert get_responses(client=client, url=detail_url) == 403
#
#
# @pytest.mark.django_db
# @pytest.mark.parametrize("payload", [
#     (payload),
#     (payload),
# ])
# def test_customer_post(payload, client, auth_client, post_responses):
#     """
#     Ensure that anybody can create a Customer.
#     Ensure that only authenticated users can get a detail information of Customers.
#     """
#     assert post_responses(client=client, url=detail_url, payload=payload).status_code == 403
#     assert post_responses(client=auth_client, url=detail_url, payload=payload).status_code == 201
#
#
# @pytest.mark.django_db
# def test_customer_details_get(client, auth_client, customer, details_customer_responses):
#     """
#     Ensure that only user and admin can get detail info about this user.
#     """
#     customer = customer(payload)
#
#     assert details_customer_responses(client=client, url=url, model=Customer, payload=payload) == 200
#     assert details_customer_responses(client=client, url=detail_url, model=Customer, payload=payload) == 403
#     assert details_customer_responses(client=auth_client, url=detail_url, model=Customer, payload=payload) == 403
#     assert details_customer_responses(client=customer, url=detail_url, model=Customer, payload=payload) == 200
#
#
# @pytest.mark.django_db
# def test_customer_delete(client, auth_client, customer, delete_customer_responses):
#     """
#     Ensure that only page owner and admin can delete a Customer.
#     """
#     customer = customer(payload)
#
#     assert delete_customer_responses(client=client, url=detail_url, model=Customer, payload=payload) == 403
#     assert delete_customer_responses(client=auth_client, url=detail_url, model=Customer, payload=payload) == 403
#     assert delete_customer_responses(client=customer, url=detail_url, model=Customer, payload=payload) == 204
#
#
# @pytest.mark.django_db
# @pytest.mark.parametrize("payload, update_payload", [
#     (payload, update_payload),
# ])
# def test_customer_put(payload, update_payload, client, customer, put_customer_responses):
#     """
#     Ensure that only page owner and admin  user can update a Customer.
#     """
#
#     customer = customer(payload)
#
#     assert put_customer_responses(
#         client=client,
#         url=detail_url,
#         model=Customer,
#         payload=payload,
#         update_payload=update_payload
#     ) == 403
#
#     assert put_customer_responses(
#         client=auth_client,
#         url=detail_url,
#         model=Customer,
#         payload=payload,
#         update_payload=update_payload
#     ) == 403
#
#     # assert put_customer_responses(
#     #     client=customer,
#     #     url=detail_url,
#     #     model=Customer,
#     #     payload=payload,
#     #     update_payload=update_payload
#     # ) == 200
import pytest
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger, FuzzyFloat
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from src.app.models import ShowroomCar, Showroom
from src.car.models import Car
from src.producer.models import ProducerCar, Producer
from src.users.models import ShowroomUser
from tests.factories import ShowroomFactory, UserFactory


@pytest.mark.django_db
def test_showroomds_car_view_set_delete_success():
    showroom = ShowroomFactory.create()
    user: ShowroomUser = UserFactory.create()
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.delete(f'/api/showroom/{showroom.id}/delete/')

    try:
        print(1, showroom.pk)
        showroom.refresh_from_db()
        pytest.fail('showroom was not deleted')
    except Showroom.DoesNotExist:
        pass


@pytest.mark.django_db
def test_showroomds_car_view_set_delete_fail():
    user: ShowroomUser = UserFactory.create()
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.delete('/api/showroom/123123123/delete/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_showroomds_car_view_set_create_success():
    payload = {
        'name': 'test',
        'specification': 1
    }
    user: ShowroomUser = UserFactory.create(is_showroom=True, is_active=True)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post('/api/showroom/create/', data=payload)
    assert response.status_code == 201
    assert response.data['name'] == payload['name']


@pytest.mark.django_db
def test_showroomds_car_view_set_create_fail_permission():
    payload = {
        'name': 'test',
        'specification': 1
    }
    user: ShowroomUser = UserFactory.create(is_showroom=False, is_active=True)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post('/api/showroom/create/', data=payload)
    assert response.status_code == 403


@pytest.mark.django_db
def test_showroomds_car_view_set_list():
    expected = 3
    ShowroomFactory.create_batch(expected)
    user: ShowroomUser = UserFactory.create(is_showroom=True, is_active=True)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get('/api/showroom/list/')
    assert response.status_code == 200
    assert len(response.data['results']) == expected


@pytest.mark.django_db
def test_showroomds_car_view_set_details():
    showroom = ShowroomFactory.create()
    user: ShowroomUser = UserFactory.create(is_showroom=True, is_active=True)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get(f'/api/showroom/{showroom.pk}/details/')
    assert response.status_code == 200
    assert response.data['Showroom details']['name'] == showroom.name
