from django.contrib import admin
from .models import TodoItem, Tag

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')  # Display these fields in the changelist
    list_filter = ('status', 'due_date')  # Filters for status and due date
    search_fields = ('title', 'description')  # Search functionality for title and description

    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'due_date', 'status')
        }),
        ('Additional Information', {
            'fields': ('tags',)
        }),
    )

    readonly_fields = ('timestamp',)  # Make timestamp field read-only


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Tag, TagAdmin)