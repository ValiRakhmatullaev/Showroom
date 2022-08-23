from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from src.users.models import ShowroomUser


class ShowroomUserSerializer(UserCreateSerializer):
    class Meta:
        model = ShowroomUser
        fields = [
            "username",
            "email",
            "password",
            "is_customer",
            "is_producer",
            "is_showroom",
        ]
