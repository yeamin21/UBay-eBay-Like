from user.models import User
from django.contrib.auth.backends import ModelBackend


class CustomBackend(ModelBackend):
    def authenticate(self, request, email):
        user, created = User.objects.get_or_create(email=email)
        return user

    def get_user(self, email):
        return super().get_user(email)
