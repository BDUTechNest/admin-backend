from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        role = user.role
        scopes = list(user.user_permissions.values("codename", "name"))
        scopes = [
            {"codename": f"{permission.codename}", "name": f"{permission.name}"}
            for permission in user.user_permissions.all()
        ]
        token = super().get_token(user)
        token["email"] = user.email
        token["role"] = role
        token["scopes"] = scopes
        return token
