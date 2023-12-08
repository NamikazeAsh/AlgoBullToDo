from django.test import TestCase
from ToDoApp.models import *
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date 

class TodoItemModelTestCase(TestCase):
    def test_todoitem_creation(self):
        todo_item = TodoItem.objects.create(title='Test Title', description='Test Description')
        self.assertIsInstance(todo_item, TodoItem)

    def test_due_date_in_past(self):
            past_date = date.today() - timezone.timedelta(days=1)
            with self.assertRaises(ValidationError):
                TodoItem.objects.create(title='Test Title', description='Test Description', due_date=past_date)

    def test_empty_title(self):
        with self.assertRaises(ValidationError):
            TodoItem.objects.create(title='', description='Test Description')

    def test_empty_description(self):
        with self.assertRaises(ValidationError):
            TodoItem.objects.create(title='Test Title', description='')

class TagModelTestCase(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name='Test Tag')
        self.assertIsInstance(tag, Tag)
        
    def test_name_accepts_numbers(self):
        # Test if the 'name' field accepts numbers
        tag_with_number = Tag.objects.create(name='Tag123')
        self.assertIsInstance(tag_with_number, Tag)
        
        # Retrieve the created tag and assert its name
        retrieved_tag = Tag.objects.get(id=tag_with_number.id)
        self.assertEqual(retrieved_tag.name, 'Tag123')

    def test_name_accepts_numerals(self):
        # Test if the 'name' field accepts numerals
        tag_with_numerals = Tag.objects.create(name='123')
        self.assertIsInstance(tag_with_numerals, Tag)
        
        # Retrieve the created tag and assert its name
        retrieved_tag = Tag.objects.get(id=tag_with_numerals.id)
        self.assertEqual(retrieved_tag.name, '123')
        
    def test_tag_str_representation(self):
        tag = Tag.objects.create(name='Test Tag')
        self.assertEqual(str(tag), 'Test Tag')