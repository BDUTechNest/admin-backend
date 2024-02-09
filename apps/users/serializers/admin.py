from rest_framework import serializers
from django.db import transaction, IntegrityError
from django.contrib.auth import authenticate, get_user_model
from apps.users.models.admin import Admin
from .user import CreateUserMixin


class RegisterAdminSerializer(CreateUserMixin, serializers.Serializer):
    default_error_messages = {"cannot_create_user": "can not create user"}
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def create(self, validated_data):
        return super().create(validated_data)
