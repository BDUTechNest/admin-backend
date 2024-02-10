from django.db.models.query import QuerySet
from apps.users.manager import UserManager
from apps.users.models.user import User, Role
from django.contrib.auth.models import Group


class NationalAuthorityManager(UserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=Role.NATIONALAUTHORITY)

    def create_user(self, email, password=None, **extra_fields):
        group, created = Group.objects.get_or_create(name="national_authority")
        return super().create_user(
            email, password, role=Role.NATIONALAUTHORITY, groups=group, **extra_fields
        )


class NationalAuthority(User):
    base_role = Role.NATIONALAUTHORITY
    objects = NationalAuthorityManager()

    class Meta:
        proxy = True
