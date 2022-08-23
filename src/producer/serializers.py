from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from src.producer.models import Producer, DiscountProducer, ProducerCar


class ProducerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = [
            "name",
            "email",
            "found_year",
            "description",
            "cars",
        ]


class ProducerCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProducerCar
        fields = ["car",
                  "producer",
                  "price",
                  "count",
                  "is_sale",
                  ]

    def get_total_cars(self, instance):
        return instance.car.count()


class DiscountProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountProducer
        fields = "__all__"
