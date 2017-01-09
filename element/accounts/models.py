from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    '''
    Fields inherited from PermissionsMixin:
    password - is_superuser - groups - permissions
    '''
    email = models.EmailField('Email Address', unique=True)
    first_name = models.CharField('First Name', max_length=30, blank=True)
    last_name = models.CharField('Last Name', max_length=30, blank=True)

    is_staff = models.BooleanField(
        'Staff Status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'Active',
        default=True,
        help_text="""
            Designates whether this user should be treated as active.
            Unselect this instead of deleting accounts.
        """
    )
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)

    instagram_handle = models.CharField('Instagram Handle', max_length=100, null=True, blank=True)
    bithdate = models.DateField('Birthdate', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        return self.email
