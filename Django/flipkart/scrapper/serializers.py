from rest_framework import serializers
from .models import Items
class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ('name', 'storage_details' ,  'screen_size' , 'camera_details' , 'battery_details' , 'processor' , 'price')