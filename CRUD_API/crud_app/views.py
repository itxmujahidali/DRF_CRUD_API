import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from requests import request
from uritemplate import partial
from .models import Student
from .serializers import StudentSerializer
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
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
    if (request.method == "POST"):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer =  StudentSerializer(data = python_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg":"Data inserted!"})
    
    if (request.method == "PUT"):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        rol = python_data.get("roll")
        stu = Student.objects.get(roll=rol)
        print(f'---------------------->',stu)
        serializer =  StudentSerializer(stu, data=python_data, partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"msg":"Data Updated!"})

    if (request.method == "DELETE"):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        rol = python_data.get("roll")
        stu = Student.objects.get(roll=rol)
        stu.delete()
        return JsonResponse({"msg":"Data Deleted!"})