from core.common_api.common_api import CustomViewSet
from core.permissions.permissions import IsShowroomUser
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import filters

from .filter import ShowroomFilter
from .models import Showroom, ShowroomCar
from .serializers import ShowroomSerializer, ShowroomsCarSerializer, ShowroomCarActionSerializer


class ShowroomsViewSet(CustomViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer
    permission_classes = [(IsAdminUser | IsShowroomUser)]
    filterset_class = ShowroomFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ("name",)

    # serializer_mapping = {
    #     'create_showroom': ShowroomSerializer,
    #     'list': ShowroomSerializer,
    #     'update': ShowroomSerializer,
    # }

    @action(methods=["get"], detail=False, url_path="list")
    def list_of_showrooms(self, request):
        return super(ShowroomsViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_showroom(self, request, pk):
        showroom_detail = Showroom.objects.get(pk=pk)
        data = ShowroomSerializer(showroom_detail).data
        return Response({"Showroom details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_showroom(self, request):
        return super(ShowroomsViewSet, self).post(request)

    @action(
        detail=True,
        methods=["delete"],
        permission_classes=[AllowAny],
        url_path="delete",
    )
    def delete(self, request, pk):
        return super(ShowroomsViewSet, self).delete(request, pk)


class ShowroomsCarViewSet(CustomViewSet):
    queryset = ShowroomCar.objects.all()
    serializer_class = ShowroomsCarSerializer
    permission_classes = [(IsAdminUser | IsShowroomUser)]
    filterset_class = ShowroomFilter
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ("name",)

    # serializer_mapping = {
    #     'create_showroom': ShowroomSerializer,
    #     'list': ShowroomSerializer,
    #     'update': ShowroomSerializer,
    # }

    @action(methods=["get"], detail=False, url_path="list")
    def list_of_showrooms(self, request):
        return super(ShowroomsCarViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_showroom(self, request, pk):
        showroom_detail = ShowroomCar.objects.get(pk=pk)
        data = ShowroomsCarSerializer(showroom_detail).data
        return Response({"Showroom details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_showroom(self, request):
        return super(ShowroomsViewSet, self).post(request)

    @action(
        detail=True,
        methods=["delete"],
        permission_classes=[AllowAny],
        url_path="delete",
    )
    def delete(self, request, pk):
        return super(ShowroomsViewSet, self).delete(request, pk)
