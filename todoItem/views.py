from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TodoItem
from .serializers import TodoSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def add_todo_item(request):
    #
    if request.method == 'GET':
        return Response({})
    
    elif request.method == 'POST':
        return Response({})