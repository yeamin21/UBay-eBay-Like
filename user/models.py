from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=250, unique=True)
    username = models.CharField(null=True, blank=True, max_length=20)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'
