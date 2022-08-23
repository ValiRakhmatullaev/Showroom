from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from src.car.serializers import CarSerializer
from src.customer.models import CustomerOrder, Customer


class CustomerOrderSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)

    class Meta:
        model = CustomerOrder
        fields = ["app", "price", "car"]


class CustomerSerializer(CountryFieldMixin, serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            "name",
            "email",
            "balance",
            "country",
            "age",
            "driver_licence",
            "customer_orders",
            "specification",
        ]


class CustomerShortInfoSerializer(CountryFieldMixin, serializers.ModelSerializer):
    number_of_purchases = serializers.IntegerField()

    class Meta:
        model = Customer
        fields = ["name", "number_of_purchases"]
