import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from requests import request
from .models import Student
from .serializers import StudentSerializer
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
# Create your views here.

def student_data(request):
    if (request.method == "GET"):
        json_data = request.body
        print(json_data)
        # return HttpResponse(json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(f'Python Data -------------->',python_data)
        user_id = python_data.get('user_id', None)
        print(f'User ID -------------->',user_id)
        if (user_id is not None):
            stu = Student.objects.get(roll = user_id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            print(f'DATA FETCHED -------------->',json_data)
            return HttpResponse(json_data, content_type="application/json")
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        print(f'ALL DATA FETCHED -------------->',json_data)
        return HttpResponse(json_data, content_type="application/json")
