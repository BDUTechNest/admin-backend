from apps.users.models.division_authority import DivisionalAuthority
from apps.users.serializers.user import CreateUserMixin
from rest_framework import serializers


class CreateDivisionalAuthorityMixin(CreateUserMixin):
    def get_model(self):
        return DivisionalAuthority


class RegisterDivisionalAuthoritySerializer(
    CreateDivisionalAuthorityMixin, serializers.Serializer
):
    default_error_messages = {"cannot_create_user": "can not create user"}
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def create(self, validated_data):
        return super().create(validated_data)
