from django.views.generic import ListView
from django.http import HttpResponse
from .models import User
from .models import Task

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


def home(request):
    return HttpResponse("Hello, world!")

def task_list(request):
    tasks = Task.objects.all()
    tasks_list = ', '.join([task.title for task in tasks])
    return HttpResponse(tasks_list)

