from django.urls import include, path
from rest_framework import routers

from src.transaction.views import TransactionShowroomToCustomerViewSet, TransactionProducerToShowroomViewSet

router = routers.DefaultRouter()
router.register(r"transaction/showroom", TransactionShowroomToCustomerViewSet)
router.register(r"transaction/producer", TransactionProducerToShowroomViewSet)

urlpatterns = [path("", include(router.urls))]
