from django.urls import include, path
from rest_framework import routers

from src.producer.views import ProducerViewSet, ProducerCarsViewSet

router = routers.DefaultRouter()
router.register(r'producer', ProducerViewSet)
router.register(r'producercar', ProducerCarsViewSet)
urlpatterns = [path("", include(router.urls))]
