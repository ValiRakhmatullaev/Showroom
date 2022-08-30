
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from src.app.serializers import ShowroomsCarSerializer
from src.car.serializers import CarSerializer
from src.customer.serializers import CustomerShortInfoSerializer
from src.transaction.models import SalesShowroomToCustomer, SalesProducerToShowroom


class SalesShowroomToBuyersSerializer(CountryFieldMixin, serializers.ModelSerializer):
    showroom = ShowroomsCarSerializer(read_only=True)
    customer = CustomerShortInfoSerializer(read_only=True)
    car = CarSerializer(read_only=True)

    class Meta:
        model = SalesShowroomToCustomer
        fields = ["showroom", "customer", "car", "price", "amount_of_discount"]


class SalesProducerToShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesProducerToShowroom
        fields = "__all__"
