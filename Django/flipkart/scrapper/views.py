from rest_framework import viewsets

from .serializers import ItemsSerializer
from .models import Items


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all().order_by('name')
    serializer_class = ItemsSerializer