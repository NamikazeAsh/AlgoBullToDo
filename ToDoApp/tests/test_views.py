from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ToDoApp.models import *
from django.contrib.auth.models import User 

class TodoItemAPITestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test123')
        self.client.force_authenticate(user=self.user)
        self.todoitem = TodoItem.objects.create(title='Test Task', description='Test Description')
        
    def test_create_todoitem_with_tags(self):
        url = reverse('todo-create')
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'tags': ['Tag1', 'Tag2', 'Tag3']  # Example tags data
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_todo_item = TodoItem.objects.get(title='New Task')
        
        # Verify if tags are associated with the created TodoItem
        self.assertEqual(created_todo_item.tags.count(), len(data['tags']))
        for tag_name in data['tags']:
            tag = Tag.objects.get(name=tag_name)
            self.assertIn(tag, created_todo_item.tags.all())

    def test_get_todoitem_list(self):
        url = reverse('todo-read-all')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), TodoItem.objects.count())

    def test_get_todoitem_detail(self):
        url = reverse('todo-read-one', kwargs={'pk': self.todoitem.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_todoitem(self):
        url = reverse('todo-update', kwargs={'pk': self.todoitem.pk})
        data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_todoitem(self):
        url = reverse('todo-delete', kwargs={'pk': self.todoitem.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        


