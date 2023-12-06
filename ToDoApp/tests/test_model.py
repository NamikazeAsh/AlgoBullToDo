from django.test import TestCase
from ToDoApp.models import *

class TodoItemModelTestCase(TestCase):
    def test_todoitem_creation(self):
        todo_item = TodoItem.objects.create(title='Test Title', description='Test Description')
        self.assertIsInstance(todo_item, TodoItem)


