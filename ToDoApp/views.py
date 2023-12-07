from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout
from .models import TodoItem
from .serializers import TodoItemSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({"detail": "Successfully logged in."})
        else:
            return Response({"detail": "Invalid credentials."}, status=400)

class UserLogoutView(APIView):
    def post(self, request):
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
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TodoItemDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "TodoItem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)