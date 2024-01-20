from rest_framework import serializers
from wapi.models import OrderItem
from .item_serial import ItemSerializer
from .order_serial import OrderSerializer

class OrderItemSerializer(serializers.ModelSerializer):
  order = OrderSerializer()
  item = ItemSerializer()
  class Meta:
    model = OrderItem
    fields = ('id', 'order', 'item')
    depth = 1
