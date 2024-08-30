"""Hola"""
from django.urls import path
from . import views

urlpatterns = [
    path('note-register/', views.note_register),
    path('get-notes/', views.get_notes),
    path('edit-note/', views.edit_note),
    path('delete-note/', views.delete_note)
]
