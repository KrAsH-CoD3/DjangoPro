from .import views
from django.contrib import admin
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    
]
 