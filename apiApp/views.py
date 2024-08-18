from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProgrammerSerializer, SaleTypeSerializer
from .models import Programmer, SaleType

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
  queryset = Programmer.objects.all()
  serializer_class = ProgrammerSerializer

class SaleTypeViewAPI(APIView):
  queryset = SaleType.objects.all()
  serializer_class = SaleTypeSerializer
  
  def get(self, request, format=None):
    sale_types = SaleType.objects.all()
    serializer = SaleTypeSerializer(sale_types, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
