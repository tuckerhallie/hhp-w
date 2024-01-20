from rest_framework import serializers
from wapi.models import PaymentType

class PaymentTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PaymentType
    fields = ('id', 'type')
