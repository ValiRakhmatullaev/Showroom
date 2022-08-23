from rest_framework import serializers

from src.car.models import Car


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
