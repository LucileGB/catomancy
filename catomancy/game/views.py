from rest_framework import viewsets
from rest_framework import permissions

from .models import Cat, Player
from .serializers import CatSerializer, PlayerSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('-name')
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('-player')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
