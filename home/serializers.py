from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    name = models.CharField(max_length=150)
    roll = models.IntegerField()
    city = models.CharField(max_length=150)
    
    def create(self,validete_data):
      return Student.objects.create(**validete_data)