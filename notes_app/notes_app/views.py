"""Hola"""
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError 
from rest_framework import status
from .serializer import UserSerializer

@csrf_exempt
def my_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            user_json = serializer.data
            return JsonResponse({"status": status.HTTP_201_CREATED, "message": "Form data received!", "usuario": user_json['username']})    
        return JsonResponse({"status": status.HTTP_400_BAD_REQUEST ,"message": "Invalid request"})
        
@csrf_exempt
def my_register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        try:
            user = User.objects.create_user(username=username, password=password, email='*')
            user.save()
            return JsonResponse({"status": status.HTTP_201_CREATED})
        except IntegrityError:
            return JsonResponse({"status": status.HTTP_400_BAD_REQUEST})

        
@csrf_exempt
def my_logout(request):
    logout(request)
    print("si cerro sesion")
    return JsonResponse({"status": status.HTTP_200_OK})