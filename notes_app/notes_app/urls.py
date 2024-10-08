"""
URL configuration for notes_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('create-account/', TemplateView.as_view(template_name='index.html')),
    path('home/<str:username>', TemplateView.as_view(template_name='index.html'), name='home'),
    path('home/<str:username>/create-note/', TemplateView.as_view(template_name='index.html')),
    path('home/<str:username>/edit-note/', TemplateView.as_view(template_name='index.html')),
    path('api-notes/', include('notes.urls')),
    path('login/', views.my_login),
    path('register/', views.my_register),
    path('logout/', views.my_logout)
]
