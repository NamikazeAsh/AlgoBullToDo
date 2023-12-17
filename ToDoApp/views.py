from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Tag,TodoItem
from .serializers import TodoItemSerializer
from django.core.exceptions import ValidationError

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
        mutable_data = request.data.copy()
        tags_data = mutable_data.pop('tags', [])

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)

        try:
            instance = serializer.save()

            for tag_name in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)

            return Response({"message": "TodoItem created successfully"}, status=status.HTTP_201_CREATED)
        
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class TodoItemUpdateView(generics.UpdateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_update(serializer)
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class TodoItemDeleteView(generics.DestroyAPIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     queryset = TodoItem.objects.all()
#     serializer_class = TodoItemSerializer

#     def destroy(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#             instance.delete()
#             return Response({"message": "TodoItem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TodoItemDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    http_method_names = ['delete']
    
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        message = "TodoItem deleted successfully!"
        response_data = {
            "detail": message
        }
        return Response(response_data,status=status.HTTP_200_OK)
