from templated_mail.mail import BaseEmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ActivationEmail(BaseEmailMessage):
    template_name = "users/activation.html"

    def get_context_data(self):
        # ActivationEmail can be deleted
        context = super().get_context_data()
        user = context.get("user")
        token, uid = get_uid_and_token_for_reset(user)
        context["uid"] = uid
        context["token"] = token
        context["url"] = "activate/{uid}/{token}/".format(**context)
        return context


def get_uid_and_token_for_reset(user):
    # try:
    uid: str = urlsafe_base64_encode(force_bytes(user.id))
    # except TypeError as type_err:
    #     raise UrlSafeEncodeError(
    #         {"message": "Error encoding the user id"}
    #     ) from type_err

    # try:
    token: str = PasswordResetTokenGenerator().make_token(user)
    # except TypeError as type_err:
    #     raise PasswordResetTokenGenerationError(
    #         {"message": "Error encoding the token"}
    #     ) from type_err

    return token, uid
