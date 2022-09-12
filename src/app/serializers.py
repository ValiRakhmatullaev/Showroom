from django.db.models import Count, F
from rest_framework import serializers

from src.app.models import Showroom, ShowroomCar


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = [
            "name",
            "email",
            "balance",
            "specification",
        ]


class ShowroomCarActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomCar
        fields = [
            "showroom",
            "car",
            "producer",
            "price",
            "count",
        ]


class ShowroomsCarSerializer(serializers.ModelSerializer):
    total_cars = serializers.SerializerMethodField()

    class Meta:
        model = ShowroomCar
        fields = [
            "showroom",
            "car",
            "producer",
            "price",
            "count",
            "total_cars",
        ]

    def get_cars(self, instance):
        cars = (
            ShowroomCar.objects.filter(showroom=instance)
                .values("price", "count")
                .annotate(total_models=Count("count"))
                .order_by()
        )
        serializer = ShowroomsCarSerializer(cars, many=True).data
        return serializer

    def get_total_cars(self, instance):
        return instance.showroom_car.all().count()

        # def get_buyers(self, instance):
        #     queryset = Showroom.objects.get(pk=instance.id)
        #     buyers = (
        #         queryset.showroom.all()
        #             .values(name=F("customer__name"))
        #             .annotate(number_of_purchases=Count("customer"))
        #             .order_by()
        #     )
        #     serializer_data = CustomerShortInfoSerializer(buyers, many=True).data
        #
        #     return serializer_data
