from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import TodoItemCreateView,TodoItemDeleteView,TodoItemReadAllView,TodoItemReadOneView,TodoItemUpdateView

urlpatterns = [
    path('todos/create/', TodoItemCreateView.as_view(), name='todo-create'),
    path('todos/<int:pk>/', TodoItemReadOneView.as_view(), name='todo-read-one'),
    path('todos/', TodoItemReadAllView.as_view(), name='todo-read-all'),
    path('todos/update/<int:pk>/', TodoItemUpdateView.as_view(), name='todo-update'),
    path('todos/delete/<int:pk>/', TodoItemDeleteView.as_view(), name='todo-delete'),

]
