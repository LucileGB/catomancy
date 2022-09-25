from rest_framework import viewsets
from rest_framework import permissions

from .models import Cat
from .serializers import CatSerializer

class CatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cat.objects.all().order_by('-name')
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticated]
