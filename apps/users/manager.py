import bcrypt
import secrets
from django.contrib.auth.models import BaseUserManager, Group, Permission
from django.db import transaction
from apps.users.models.password import SaltedPasswordModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.special_key = user.generate_special_key()

        salt = bcrypt.gensalt()
        user.salt = salt

        hashed_special_key = bcrypt.hashpw(user.special_key, salt)
        password_obj = SaltedPasswordModel(hashed_special_key=hashed_special_key)

        if password is None:
            self.password = secrets.token_urlsafe(13)
            password_obj.set_password(self.password)
        else:
            password_obj.set_password(password)

        with transaction.atomic():
            password_obj.save(using=self._db)
            user.save(using=self._db)
            # if self.permissions is not None:
            #     user.user_permissions.set(self.permissions)
            #     user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        group, created = Group.objects.get_or_create(name="super_admin")
        group.permissions.set(Permission.objects.all())
        group.save()
        user = self._create_user(email, password, groups=group, **extra_fields)
        print("your password is: ", self.password)
        return user
