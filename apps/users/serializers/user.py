from django.db import IntegrityError, transaction
from rest_framework import serializers

# from django.db.models import
from apps.users.models.user import User


class CreateUserMixin:
    model = None

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "user already exists"})
        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = self.model.objects.create_user(
                email=validated_data.get("email"),
                password=validated_data.get("password"),
                phone=validated_data.get("phone"),
            )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone", "role"]
