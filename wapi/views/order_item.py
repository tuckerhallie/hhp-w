from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from wapi.models import OrderItem, Order, Item
from wapi.serializers import OrderItemSerializer

class OrderItemView(ViewSet):
  
  def retrieve(self, request, pk):
    try:
      order_item = OrderItem.objects.get(pk=pk)
      serializer = OrderItemSerializer(order_item)
      return Response(serializer.data)
    except OrderItem.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    order_items = OrderItem.objects.all()
    serializer = OrderItemSerializer(order_items, many=True)
    return Response(serializer.data)
  
  
  
  def create(self, request):
      try:
          order = get_object_or_404(Order, pk=request.data["order_id"])
          item = get_object_or_404(Item, pk=request.data["item_id"])
          order_item = OrderItem.objects.create(order=order, item=item)
          serializer = OrderItemSerializer(order_item)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      except ValidationError as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
      
  @action(detail=True, methods=['get'])
  def items_for_order(self, request, pk=None):
      if pk is not None:
          order_items = OrderItem.objects.filter(order_id=pk)
          serializer = OrderItemSerializer(order_items, many=True)
          return Response(serializer.data)
      else:
          return Response({'message': 'Order ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
  def destroy(self, request, pk=None):
    try:
        order_item = get_object_or_404(OrderItem, pk=pk)
        order_item.delete()
        return Response({'message': 'Order item deleted'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
  
