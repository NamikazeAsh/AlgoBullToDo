from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class TodoItem(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(default=timezone.now() + timezone.timedelta(days=1), null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    
    def clean(self):
        super().clean()
        if self.due_date and self.due_date < timezone.now().date():
            raise ValidationError("Due date cannot be in the past.")
        if not self.title.strip():
            raise ValidationError("Title cannot be empty.")
        if not self.description.strip():
            raise ValidationError("Description cannot be empty.")

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name