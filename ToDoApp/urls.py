from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('todos/create/', TodoItemCreateView.as_view(), name='todo-create'),
    path('todos/<int:pk>/', TodoItemReadOneView.as_view(), name='todo-read-one'),
    path('todos/', TodoItemReadAllView.as_view(), name='todo-read-all'),
    path('todos/update/<int:pk>/', TodoItemUpdateView.as_view(), name='todo-update'),
    path('todos/delete/<int:pk>/', TodoItemDeleteView.as_view(), name='todo-delete'),

]
