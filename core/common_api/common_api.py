from rest_framework import status, viewsets
from rest_framework.response import Response


class CustomViewSet(viewsets.GenericViewSet):
    search_fields = None

    def get(self, request):
        page = self.paginate_queryset(self.filter_queryset(self.queryset))
        if page is not None:
            serializer = self.get_serializer_class()
            serializer = serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        serializer = self.get_serializer_class()
        serializer = serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @property
    def paginator(self):
        if not hasattr(self, "_paginator"):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    # def get_serializer_class(self):
    #     default_serializer = self.serializer_class
    #     serializer_mapping = self.serializer_mapping
    #
    #     if serializer_mapping:
    #         return serializer_mapping.get(self.action, default_serializer)
    #
    #     return default_serializer
