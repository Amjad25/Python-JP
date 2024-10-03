from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view

from .models import Category

@api_view(['GET'])
def get_all_categories(request:Request):

    categories = Category.objects.all()
    return Response(categories.values() , status=status.HTTP_200_OK)