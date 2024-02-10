from django.db.models.query import QuerySet
from apps.users.manager import UserManager
from apps.users.models.user import User, Role
from django.db.models import Q
from django.contrib.auth.models import Permission


class TeacherManager(UserManager):
    permissions = Permission.objects.filter(
        Q(codename__endswith="teacher") | Q(codename__endswith="course")
    )

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=Role.TEACHER)


class Teacher(User):
    base_role = Role.TEACHER
    objects = TeacherManager()

    class Meta:
        proxy = True
