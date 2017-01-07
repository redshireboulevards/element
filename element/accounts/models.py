from django.db import models
from django.contrib.auth.models import AbstractUser

from users.managers import UserManager


class User(AbstractUser):
    '''
    Fields inherited from django base user model:
    password - first_name - last_name - is_active - is_superuser
    groups - permissions
    '''
    email = models.EmailField('email address', unique=True)

    instagram_handle = models.CharField('Instagram Handle', max_length=100, null=False, blank=True, unique=True)
    bithdate = models.DateField('Birthdate', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return super().get_full_name() or self.email
