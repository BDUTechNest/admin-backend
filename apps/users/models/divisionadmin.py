from django.db.models.query import QuerySet
from apps.users.manager import UserManager
from .user import User, Role
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, Permission


class DivisionAdminManager(UserManager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset(*args, **kwargs).filter(role=Role.DIVISIONALADMIN)

    def create_user(self, email, password=None, **extra_fields):
        group, created = Group.objects.get_or_create(name="divisional_admin")
        return super().create_user(
            email, password, role=Role.DIVISIONALADMIN, groups=group, **extra_fields
        )


class DivisionalAdmin(User):
    base_role = Role.DIVISIONALADMIN
    objects = DivisionAdminManager()

    class Meta:
        proxy = True
