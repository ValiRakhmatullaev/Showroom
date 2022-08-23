from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, path
from rest_framework import routers

from src.customer.views import CustomerViewSet, CustomerOrderViewSet

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'customerorder', CustomerOrderViewSet)
urlpatterns = [path("", include(router.urls))]

# urlpatterns = format_suffix_patterns(urlpatterns)
