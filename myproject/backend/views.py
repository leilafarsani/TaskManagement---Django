from django.views.generic import ListView
from django.http import HttpResponse
from .models import User

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


def home(request):
    return HttpResponse("Hello, world!")


