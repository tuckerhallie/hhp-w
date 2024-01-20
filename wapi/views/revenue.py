from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from wapi.models import Revenue
from wapi.serializers import RevenueSerializer

class RevenueView(ViewSet):
    def retrieve(self, request, pk):
      revenue = Revenue.objects.get(pk=pk)
      serializer = RevenueSerializer(revenue)
      return Response(serializer.data)
    
    def list(self, request):
        revenues = Revenue.objects.all()
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)
      
    def create(self, request):
      serializer = RevenueSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
