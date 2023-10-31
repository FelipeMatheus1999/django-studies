# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Local

from apps.account.managers import CustomUserManager


class AccountModel(AbstractUser):
    objects = CustomUserManager()

    email = models.EmailField(_('email address'), unique=True, blank=True)

    EMAIL_FIELD = 'username'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
