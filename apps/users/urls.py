from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.views import (
    RegisterView,
    DivisionalAdminViewSet,
    DivisionAuthorityViewSet,
    NationalAdminViewSet,
    NationalAuthorityViewSet,
)
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("division/admins", DivisionalAdminViewSet, basename="division-admin")
router.register(
    "division/authorities", DivisionAuthorityViewSet, basename="division-authority"
)
router.register("national/admin", NationalAdminViewSet, basename="national-admin")
router.register(
    "national/authorities", NationalAuthorityViewSet, basename="national-authority"
)

urlpatterns = [
    # path("test/register/", RegisterView.as_view()),
    # path("login/", TokenObtainPairView.as_view()),
    path("", include(router.urls)),
]
