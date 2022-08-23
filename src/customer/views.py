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
from src.customer.filter import CustomerFilter
from src.customer.models import Customer, CustomerOrder
from src.customer.serializers import CustomerSerializer, CustomerOrderSerializer
from rest_framework import filters


class CustomerViewSet(CustomViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [(IsProducerUser | IsAdminUser)]
    filterset_class = CustomerFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ("name",)

    @action(
        methods=["get"],
        detail=False,
        url_path="list",
    )
    def list_of_customers(self, request):
        return super(CustomerViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def customer_of_dealer(self, request, pk):
        customer_detail = Customer.objects.get(pk=pk)
        data = CustomerSerializer(customer_detail).data
        return Response({"customer details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_customer(self, request):
        return super(CustomerViewSet, self).post(request)

    # TODO: remake function, do not delete instance, change is_active field to False
    @action(detail=True, methods=["delete"], url_path="delete")
    def delete(self, request, pk):
        return super(CustomerViewSet, self).delete(request, pk)


class CustomerOrderViewSet(CustomViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
    permission_classes = [(IsProducerUser | IsAdminUser)]
    filterset_class = CustomerFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ("name",)

    @action(
        methods=["get"],
        detail=False,
        url_path="list",
    )
    def list_of_customer_orders(self, request):
        return super(CustomerOrderViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_customer_orders(self, request, pk):
        order_detail = CustomerOrder.objects.get(pk=pk)
        data = CustomerOrderSerializer(order_detail).data
        return Response({"CustomerOrderSerializercer_car details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_customer_order(self, request):
        return super(CustomerOrderViewSet, self).post(request)

    @action(detail=True, methods=["delete"], url_path="delete")
    def delete(self, request, pk):
        return super(CustomerOrderViewSet, self).delete(request, pk)

