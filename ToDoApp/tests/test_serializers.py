from django.test import TestCase
from ToDoApp.serializers import TodoItemSerializer

# --------------------------------- Unit test -------------------------------- #

class TodoItemSerializerTestCase(TestCase):
    def test_todoitem_serializer(self):
        todo_item_data = {'title': 'Sample Title', 'description': 'Sample Description'}
        serializer = TodoItemSerializer(data=todo_item_data)
        self.assertTrue(serializer.is_valid())


