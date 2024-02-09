from apps.users.models.division_authority import DivisionalAuthority
from apps.users.models.division_admin import DivisionalAdmin
from apps.users.models.national_authority import NationalAuthority
from apps.users.permissions import CustomDjangoModelPermissions
from apps.users.serializers.user import UserSerializer
from rest_framework.viewsets import ModelViewSet


class DivisionalAdminViewSet(ModelViewSet):
    queryset = DivisionalAdmin.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomDjangoModelPermissions]


class NationalAuthorityViewSet(ModelViewSet):
    queryset = NationalAuthority.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomDjangoModelPermissions]


class DivisionAuthorityViewSet(ModelViewSet):
    queryset = DivisionalAuthority.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomDjangoModelPermissions]
