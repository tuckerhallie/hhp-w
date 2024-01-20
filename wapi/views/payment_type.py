from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from wapi.models import PaymentType
from wapi.serializers import PaymentTypeSerializer

class PaymentTypeView(ViewSet):
  def retrieve(self, request, pk):
    try:
      payment_type = PaymentType.objects.get(pk=pk)
      serializer = PaymentTypeSerializer(payment_type)
      return Response(serializer.data)
    except PaymentType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    payment_types = PaymentType.objects.all()
    serializer = PaymentTypeSerializer(payment_types, many=True)
    return Response(serializer.data)
