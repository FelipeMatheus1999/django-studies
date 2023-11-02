# Django
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_active=True)
