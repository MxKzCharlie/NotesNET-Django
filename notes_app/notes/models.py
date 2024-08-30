"""Hola"""
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_notes')

    class Meta:
        ordering = ['date']