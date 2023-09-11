from django.shortcuts import render
import io
from django.http import HttpResponse
from .serializers import StudentSerializer
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def student_create(request):

    if request.method == 'POST':
      json_data = request.body # the function extracts the JSON data from the request body (request.body) returns bytes.
      print(json_data) # b'{"name": "Mufees", "roll": 127, "city": "Calicut"}'
      stream = io.BytesIO(json_data) 
      print(type(stream))
      print(stream)
      python_data = JSONParser().parse(stream) # This step converts the JSON data into a Python dictionary,
      serializer = StudentSerializer(data = python_data)
      if serializer.is_valid():
          serializer.save()
          res = {'msg': 'Data is Created'}
          json_data = JSONRenderer().render(res)
      else :
          json_data = JSONRenderer().render(serializer.errors)
      return HttpResponse(json_data,content_type = 'application/json')
      
      
