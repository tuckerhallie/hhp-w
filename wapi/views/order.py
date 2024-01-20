from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from wapi.models import Order, OrderType, OrderItem, User
from wapi.serializers import OrderSerializer, OrderItemSerializer

class OrderView(ViewSet):
    def retrieve(self, request, pk):
      try: 
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
      except Order.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
    def list(self, request):
      try:
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
      except Order.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
    def create(self, request):
        user = User.objects.get(uid=request.data["user"])
        order_type = OrderType.objects.get(pk=request.data["orderType"])
        
        order = Order.objects.create(
          user = user,
          name = request.data["name"],
          customer_phone = request.data["customerPhone"],
          customer_email = request.data["customerEmail"],
          order_type = order_type,
          is_closed = False,
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def update(self, request, pk):
      order = Order.objects.get(pk=pk)
      order.name = request.data.get("name", order.name)
      order.customer_phone = request.data.get("customerPhone", order.customer_phone)
      order.customer_email = request.data.get("customerEmail", order.customer_email)
      user = User.objects.get(uid=request.data["user"])
      order.user = user
      
      order_type = OrderType.objects.get(pk=request.data["orderType"])
      order.order_type = order_type
      
      is_closed = False
      order.is_closed = is_closed
      
      order.save()
      serializer = OrderSerializer(order)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)                                         
