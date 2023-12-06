from django.shortcuts import render
from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemCreateView(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemReadOneView(generics.RetrieveAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemReadAllView(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemUpdateView(generics.UpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemDeleteView(generics.DestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer