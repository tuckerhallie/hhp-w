from rest_framework import serializers
from wapi.models import OrderType

class OrderTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderType
    fields = ('id', 'label')
