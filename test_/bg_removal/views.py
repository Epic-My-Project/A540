from rest_framework import viewsets
from rest_framework.response import Response
from .Serializers import AccountsSerializer
from .models import Accounts

class AccountsViewset(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer



