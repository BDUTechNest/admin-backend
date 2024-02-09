from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.users.models.divisionauthority import DivisionalAuthority
from apps.users.models.divisionadmin import DivisionalAdmin
from apps.users.models.admin import Admin
from apps.users.models.nationaladmin import NationalAdmin
from apps.users.models.nationalauthority import NationalAuthority

from apps.users.models.user import User
from apps.users.serializers.user import UserSerializer
from .serializers.admin import RegisterAdminSerializer
from utils.email import ActivationEmail
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions, DjangoObjectPermissions
from django.contrib.auth.backends import ModelBackend


class CustomDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self) -> None:
        self.perms_map["GET"] = ["%(app_label)s.view_%(model_name)s"]


class NationalAdminViewSet(ModelViewSet):
    queryset = NationalAdmin.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomDjangoModelPermissions]


class DivisionalAdminViewSet(ModelViewSet):
    queryset = DivisionalAdmin.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomDjangoModelPermissions]


class NationalAuthorityViewSet(ModelViewSet):
    queryset = NationalAuthority.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomDjangoModelPermissions]


class DivisionAuthorityViewSet(ModelViewSet):
    queryset = DivisionalAuthority.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomDjangoModelPermissions]


class RegisterView(APIView):
    serializer_class = RegisterAdminSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        ActivationEmail(request, {"user": user}).send(to=[user.email])
        return Response({"detail": "user creation success"})
