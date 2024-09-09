from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_users, name='get_users'),
    path('add/', views.create_user, name='create_user')
]