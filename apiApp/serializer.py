from rest_framework import serializers
from .models import Programmer, SaleType

class ProgrammerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Programmer
    # fields=('fullname', 'nickname')
    fields = '__all__'
    
class SaleTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = SaleType
    fields = '__all__'