# from typing import Any
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.http.request import HttpRequest
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.serializers import TokenObtainSerializer
# from django.contrib.auth.backends import ModelBackend, UserModel


# class CustomAuthentication(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs: Any):
#         try:
#             user = UserModel.objects.get(email=email)
#         except UserModel.DoesNotExist:
#             return None

#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user
#         else:
#             return None
