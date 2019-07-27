from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import exceptions


class AuthenticateUsernameEmail(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):  # NOQA
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))  # NOQA
        except UserModel.DoesNotExist:
            raise exceptions.NotFound(detail='username or email is incorrect')
        else:
            if user.check_password(password):
                return user
            else:
                raise exceptions.NotFound(detail='password is incorrect')
        return None
