from rest_condition import Or
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from core.common_api.common_api import CustomViewSet
from core.permissions.permissions import IsProducerUser
from src.producer.filter import ProducerFilter
from src.producer.models import Producer, ProducerCar
from src.producer.serializers import ProducerSerializer, ProducerCarSerializer
from rest_framework import filters


class ProducerViewSet(CustomViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [(IsProducerUser | IsAdminUser)]
    filterset_class = ProducerFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ("name",)

    @action(
        methods=["get"],
        detail=False,
        url_path="list",
    )
    def list_of_producers(self, request):
        return super(ProducerViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_producer(self, request, pk):
        producer_detail = Producer.objects.get(pk=pk)
        data = ProducerSerializer(producer_detail).data
        return Response({"producer details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_producer(self, request):
        return super(ProducerViewSet, self).post(request)

    # TODO: remake function, do not delete instance, change is_active field to False
    @action(detail=True, methods=["delete"], url_path="delete")
    def delete(self, request, pk):
        return super(ProducerViewSet, self).delete(request, pk)


class ProducerCarsViewSet(CustomViewSet):
    queryset = ProducerCar.objects.all()
    serializer_class = ProducerCarSerializer
    permission_classes = [(IsProducerUser | IsAdminUser)]
    filterset_class = ProducerFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ("name",)

    @action(
        methods=["get"],
        detail=False,
        url_path="list",
    )
    def list_of_producer_cars(self, request):
        return super(ProducerCarsViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_producer_cars(self, request, pk):
        producer_cars_detail = ProducerCar.objects.get(pk=pk)
        data = ProducerCarSerializer(producer_cars_detail).data
        return Response({"producer_car details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_producer_car(self, request):
        return super(ProducerCarsViewSet, self).post(request)

    @action(detail=True, methods=["delete"], url_path="delete")
    def delete(self, request, pk):
        return super(ProducerCarsViewSet, self).delete(request, pk)

