from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from apps.users.serializers.divisional_authority import (
    RegisterDivisionalAuthoritySerializer,
)


class RegisterDivisionalAuthorityViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = RegisterDivisionalAuthoritySerializer
