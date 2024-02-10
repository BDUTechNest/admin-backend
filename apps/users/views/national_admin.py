from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from apps.users.models.national_admin import NationalAdmin
from apps.users.permissions import CustomDjangoModelPermissions
from apps.users.serializers.national_admin import RegisterNationalAdminSerializer
from rest_framework.viewsets import ModelViewSet
from apps.users.serializers.user import UserSerializer


class RegisterNationalAdminViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = RegisterNationalAdminSerializer


class NationalAdminViewSet(ModelViewSet):
    queryset = NationalAdmin.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomDjangoModelPermissions]
