from rest_framework import serializers
from wapi.models import Revenue

class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
      model = Revenue
      fields = ('id', 'order', 'tip', 'payment_type', 'date')
