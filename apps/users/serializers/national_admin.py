from rest_framework import serializers
from apps.users.models.national_admin import NationalAdmin
from apps.users.models.user import CreateUserMixin


class CreateNationalAdminMixin(CreateUserMixin):
    def get_model(self):
        return NationalAdmin


class RegisterNationalAdminSerializer(CreateNationalAdminMixin, serializers.Serializer):
    default_error_messages = {"cannot_create_user": "can not create user"}
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def create(self, validated_data):
        return super().create(validated_data)
