from django.db.models.query import QuerySet
from apps.users.manager import UserManager
from .user import User, Role
from django.db.models import Q
from django.contrib.auth.models import Permission


class AdminManager(UserManager):
    # permissions = Permission.objects.filter(
    #     Q(codename__endswith="admin") | Q(codename__endswith="teacher")
    # )

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=Role.ADMIN)


class Admin(User):
    base_role = Role.ADMIN
    objects = AdminManager()

    class Meta:
        proxy = True
