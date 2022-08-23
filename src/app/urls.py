from django.urls import include, path
from rest_framework import routers

from src.app.views import ShowroomsViewSet, ShowroomsCarViewSet

router = routers.DefaultRouter()
router.register(r'showroom', ShowroomsViewSet)
router.register(r'showroomcar', ShowroomsCarViewSet)
urlpatterns = [path("", include(router.urls))]
