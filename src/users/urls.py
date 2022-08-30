from rest_framework import routers

from src.users.views import ShowroomUserViewSet

router = routers.DefaultRouter()
router.register(r"showroom_user", ShowroomUserViewSet, basename="showroom_user")

urlpatterns = router.urls
