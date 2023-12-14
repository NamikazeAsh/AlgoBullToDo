from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Tag,TodoItem
from .serializers import TodoItemSerializer
from rest_framework.exceptions import ValidationError

class TodoItemReadOneView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemReadAllView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemCreateView(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Perform custom clean validations
        due_date = serializer.validated_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise ValidationError({"due_date": ["Due date cannot be in the past."]})

        title = serializer.validated_data.get('title', '').strip()
        if not title:
            raise ValidationError({"title": ["Title cannot be empty."]})

        description = serializer.validated_data.get('description', '').strip()
        if not description:
            raise ValidationError({"description": ["Description cannot be empty."]})

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class TodoItemUpdateView(generics.UpdateAPIView):
    authentication_classes = [BasicAuthentication]
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
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "TodoItem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
