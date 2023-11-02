# Rest Framework
from rest_framework import serializers

# Local
from apps.account.models import AccountModel


class CreateUserPictureSerializer(serializers.Serializer):
    class Meta:
        model = AccountModel
        fields = ("picture",)
