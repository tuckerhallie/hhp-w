from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from wapi.models import OrderType
from wapi.serializers import OrderTypeSerializer

class OrderTypeView(ViewSet):

  def retrieve(self, request, pk):
    try:
      order_type = OrderType.objects.get(pk=pk)
      serializer = OrderTypeSerializer(order_type)
      return Response(serializer.data)
    except OrderType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
  def list(self, request):
    order_types = OrderType.objects.all()
    serializer = OrderTypeSerializer(order_types, many=True)
    return Response(serializer.data)
