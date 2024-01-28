from django.views.generic import ListView
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Task
from .serializers import TaskSerializer  # Import the Task serializer

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


def home(request):
    return HttpResponse("Hello, world!")

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


