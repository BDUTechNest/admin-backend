from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.views.divisional_admin import RegisterDivisionalAdminViewSet
from apps.users.views.divisional_authority import RegisterDivisionalAuthorityViewSet
from apps.users.views.national_admin import RegisterNationalAdminViewSet
from apps.users.views.national_authority import RegisterNationalAuthorityViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
# router.register("division/admins", DivisionalAdminViewSet, basename="division-admin")
# router.register(
#     "division/authorities", DivisionAuthorityViewSet, basename="division-authority"
# )

# router.register("national/admin", NationalAdminViewSet, basename="national-admin")
# router.register(
#     "national/authorities", NationalAuthorityViewSet, basename="national-authority"
# )
router.register(
    "admins/national/register",
    RegisterNationalAdminViewSet,
    basename="national-admin-register",
),
router.register(
    "authorities/national/register",
    RegisterNationalAuthorityViewSet,
    basename="national-authorities-register",
)
router.register(
    "admins/divisional/register",
    RegisterDivisionalAdminViewSet,
    basename="divisional-admins-register",
)
router.register(
    "authorities/divisional/register",
    RegisterDivisionalAuthorityViewSet,
    basename="divisional-authorities-register",
)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("", include(router.urls)),
]
