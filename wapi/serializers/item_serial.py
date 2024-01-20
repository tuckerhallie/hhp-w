from rest_framework import serializers
from wapi.models import Item

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = ('id', 'name', 'price')
