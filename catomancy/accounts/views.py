from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions

from .models import Account
from .serializers import AccountSerializer, GroupSerializer

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]