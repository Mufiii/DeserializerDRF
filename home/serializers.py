from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=150)
    
    def create(self,validete_data):
      return Student.objects.create(**validete_data)