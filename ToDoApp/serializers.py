from rest_framework import serializers
from .models import TodoItem, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = TodoItem
        fields = '__all__'
        error_messages = {
            'due_date': {
                'invalid': "Due date cannot be in the past."
            },
            'title': {
                'blank': "Title cannot be empty."
            },
            'description': {
                'blank': "Description cannot be empty."
            }
        }