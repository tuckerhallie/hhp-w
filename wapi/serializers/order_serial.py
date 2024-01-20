from rest_framework import serializers
from wapi.models import Order

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ('id', 'user', 'name', 'customer_phone', 'customer_email', 'order_type', 'is_closed')
    depth = 1
