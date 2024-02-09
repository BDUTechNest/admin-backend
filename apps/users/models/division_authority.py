from django.db.models.query import QuerySet
from apps.users.manager import UserManager
from .user import User, Role
from django.contrib.auth.models import Group


class DivisionalAuthorityManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        group, created = Group.objects.get_or_create(name="divisional_authority")
        return super().create_user(
            email, password, role=Role.DIVISIONALAUTHORITY, groups=group, **extra_fields
        )

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=Role.NATIONALAUTHORITY)


class DivisionalAuthority(User):
    base_role = Role.NATIONALAUTHORITY
    objects = DivisionalAuthorityManager()

    class Meta:
        proxy = True
