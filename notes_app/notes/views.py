"""Hola"""
import json
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Note
from .serializer import NoteSerializer

@csrf_exempt
def note_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        text = data.get('content')
        username = data.get('user')

        user = User.objects.get(username=username)

        note = Note(title=title, text=text, usuario=user)
        note.save()

        return  JsonResponse({"status": status.HTTP_201_CREATED})
    return JsonResponse({"status":status.HTTP_400_BAD_REQUEST})

@csrf_exempt
def get_notes(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        user = User.objects.get(username=username)
        notes = Note.objects.filter(usuario_id=user.pk)
        serializer = NoteSerializer(notes, many=True)
        
        return JsonResponse({"status": status.HTTP_200_OK, "data": serializer.data})
    return JsonResponse({"status": status.HTTP_400_BAD_REQUEST})

@csrf_exempt
def edit_note(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        title = data.get('title')
        content = data.get('content')
        id = data.get('id')

        note = Note.objects.get(id=id)
        note.title = title
        note.text = content
        note.save()

        return JsonResponse({"status": status.HTTP_200_OK})
    return JsonResponse({"status": status.HTTP_400_BAD_REQUEST})

@csrf_exempt
def delete_note(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        note_id = data.get('id')

        note = Note.objects.get(id=note_id)
        note.delete()

        return JsonResponse({"status": status.HTTP_200_OK})
    return JsonResponse({"status": status.HTTP_400_BAD_REQUEST})
        

        
        


