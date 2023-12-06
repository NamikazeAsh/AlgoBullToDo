from django.shortcuts import render
from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class TodoItemCreateView(generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "TodoItem created successfully"}, status=status.HTTP_201_CREATED)

class TodoItemReadOneView(generics.RetrieveAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemReadAllView(generics.ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemUpdateView(generics.UpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({"message": "TodoItem updated successfully"}, status=status.HTTP_200_OK)

class TodoItemDeleteView(generics.DestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "TodoItem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)