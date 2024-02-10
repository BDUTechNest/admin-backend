from django.db.models.query import QuerySet
from apps.users.manager import UserManager
from apps.users.models.user import User, Role
from django.contrib.auth.models import Group, Permission
from django.db.models import Q


national_authority_permissions = Q(codename__endswith="authority")


class NationalAdminManager(UserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=Role.NATIONAL_ADMIN)

    def create_user(self, email, password=None, **extra_fields):
        group, created = Group.objects.get_or_create(name="national_admin")
        return super().create_user(
            email, password, role=Role.NATIONAL_ADMIN, groups=group, **extra_fields
        )


class NationalAdmin(User):
    base_role = Role.NATIONAL_ADMIN
    objects = NationalAdminManager()

    class Meta:
        proxy = True
