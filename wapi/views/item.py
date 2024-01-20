from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from wapi.models import Item
from wapi.serializers import ItemSerializer

class ItemView(ViewSet):
  
  def retrieve(self, request, pk):
    
    try:
      item = Item.objects.get(pk=pk)
      serializer = ItemSerializer(item)
      return Response(serializer.data)
    except Item.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
