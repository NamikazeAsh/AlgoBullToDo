from django.shortcuts import render
from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import logout


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        Token.objects.get_or_create(user=user)
        return Response({"token": user.auth_token.key})


class UserLogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"detail": "Successfully logged out."})


class TodoItemReadOneView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemReadAllView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "TodoItem created successfully"}, status=status.HTTP_201_CREATED)

class TodoItemUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({"message": "TodoItem updated successfully"}, status=status.HTTP_200_OK)

class TodoItemDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "TodoItem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)