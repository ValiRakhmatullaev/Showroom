from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from core.common_api.common_api import CustomViewSet
from core.permissions.permissions import IsShowroomUser, IsCustomerUser, IsProducerUser
from src.transaction.models import SalesShowroomToCustomer, SalesProducerToShowroom
from src.transaction.serializers import SalesShowroomToBuyersSerializer


class TransactionShowroomToCustomerViewSet(CustomViewSet):
    """View for transactions from Showroom to customer"""

    queryset = SalesShowroomToCustomer.objects.all()
    serializer_class = SalesShowroomToBuyersSerializer
    permission_classes = [(IsShowroomUser | IsCustomerUser | IsAdminUser)]

    @action(methods=["get"], detail=False, url_path="history")
    def list_of_transactions(self, request):
        """Return transactions list from Showroom to customers"""
        return super(TransactionShowroomToCustomerViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="showroom-details")
    def showroom_to_customer_transaction_history(self, request, pk):
        showroom_transaction = SalesShowroomToCustomer.objects.filter(showroom=pk)
        serializer_data = SalesShowroomToBuyersSerializer(
            showroom_transaction, many=True
        ).data
        return Response(
            {"Transaction history for showroom": serializer_data},
            status=status.HTTP_200_OK,
        )

    @action(methods=["get"], detail=True, url_path="customer-details")
    def details_of_transaction(self, request, pk):
        """Return list of customer transactions"""
        customers_transactions = SalesShowroomToCustomer.objects.filter(customer=pk)
        data = SalesShowroomToBuyersSerializer(customers_transactions, many=True).data
        return Response(
            {"Transaction history for customer": data}, status=status.HTTP_200_OK
        )


class TransactionDealerToShowroomViewSet(CustomViewSet):
    queryset = SalesProducerToShowroom.objects.all()
    serializer_class = SalesShowroomToBuyersSerializer
    permission_classes = [(IsProducerUser | IsShowroomUser | IsAdminUser)]

    @action(methods=["get"], detail=False, url_path="history")
    def list_of_transactions(self, request):
        """Return transactions list from Producer to Showroom"""
        return super(TransactionDealerToShowroomViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def details_of_transaction(self, request, pk):
        """Return list of customer transactions"""
        dealers_transactions = SalesProducerToShowroom.objects.filter(dealer=pk)
        data = SalesShowroomToBuyersSerializer(dealers_transactions, many=True).data
        return Response(
            {"Transaction history to producer": data}, status=status.HTTP_200_OK
        )
