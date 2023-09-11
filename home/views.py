from django.shortcuts import render
import io
from django.http import HttpResponse
from .serializers import StudentSerializer
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
# Create your views here.

def student_create(request):

    if request.method == 'POST':
      json_data = request.body
      stream = io.BytesIO(json_data)
      python_data = JSONParser().parse(stream)
      serializer = StudentSerializer(data = python_data)
      if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Data is Created'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')
      
      json_data = JSONRenderer().render(serializer.errors)
      return HttpResponse(json_data,content_type = 'application/json')
      
      
