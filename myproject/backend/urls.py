from django.urls import path
from .views import UserListView
from . import views

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('tasks/', views.task_list, name='task_list'),
    # I will add other paths for creating, updating, and deleting tasks, and etc later
]
   
