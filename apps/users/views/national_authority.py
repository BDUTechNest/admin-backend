from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from apps.users.models.national_admin import NationalAdmin
from apps.users.permissions import CustomDjangoModelPermissions
from apps.users.serializers.national_authority import (
    RegisterNationalAuthoritySerializer,
)
from rest_framework.viewsets import ModelViewSet
from apps.users.serializers.user import UserSerializer


class RegisterNationalAuthorityViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = RegisterNationalAuthoritySerializer
