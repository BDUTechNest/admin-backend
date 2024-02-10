from collections.abc import Iterable
import bcrypt
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group
from django.db import models
from django.utils import timezone
from apps.users.manager import UserManager
from apps.users.models.password import SaltedPasswordModel


class Role(models.TextChoices):
    NATIONALAUTHORITY = "NATIONALAUTHORITY", "National Authority"
    NATIONALADMIN = "NATIONALADMIN", "National Admin"
    DIVISIONALAUTHORITY = "DIVISIONALAUTHORITY", "Divisional Authority"
    DIVISIONALADMIN = "DIVISIONALADMIN", "Divisional Admin"
    OTHER = "OTHER", "Other"
    ADMIN = "ADMIN", "Admin"
    TEACHER = "TEACHER", "Teacher"


class User(AbstractBaseUser, PermissionsMixin):
    base_role = Role.OTHER
    permissions = None
    password = None
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=10, unique=True, null=False, blank=False)
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    is_active = models.BooleanField(
        default=False,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    salt = models.BinaryField(max_length=255)
    special_key = models.BinaryField(max_length=255, unique=True)
    role = models.CharField(max_length=50, choices=Role.choices)
    groups = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="user_set",
        related_query_name="user",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = USERNAME_FIELD

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super(User, self).save(*args, **kwargs)
        else:
            return super(User, self).save(*args, **kwargs)

    objects = UserManager()

    def check_password(self, raw_password):
        special_key = self.special_key
        hashed_special_key = bcrypt.hashpw(special_key, self.salt)
        password_obj = SaltedPasswordModel.objects.get(
            hashed_special_key=hashed_special_key
        )
        if password_obj is not None:
            check_password = bcrypt.checkpw(
                raw_password.encode(), password_obj.password
            )
            if check_password:
                return True
            else:
                return False
        return False

    def generate_special_key(self) -> bytes:
        """
        Generates a special key for the user.
        """
        salt = bcrypt.gensalt()

        return bcrypt.hashpw(self.email.encode("utf-8"), salt)


# F4UvUiaRNwswS8MXAQ
