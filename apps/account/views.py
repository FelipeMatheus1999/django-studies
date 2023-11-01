# Rest Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

# Local
from apps.account.models import AccountModel
from apps.account.serializers import CreateUserPictureSerializer


class AccountViewSet(GenericViewSet, CreateModelMixin):
    queryset = AccountModel.objects.all()
    serializer_class = CreateUserPictureSerializer
