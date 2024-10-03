from django.contrib import admin
from django.urls import path,include
from .views import get_all_categories

urlpatterns = [
    path('categories', get_all_categories),
]
