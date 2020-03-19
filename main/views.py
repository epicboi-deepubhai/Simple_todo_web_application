from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Todo
from django.http import HttpResponseRedirect


def index(request):
    todo_items = Todo.objects.all().order_by('-time_added')
    return render(request, 'main/index.html', {'todo_items': todo_items})


@csrf_exempt
def add_todo(request):
    date_current = timezone.now()
    text = request.POST['content']
    Todo.objects.create(time_added=date_current, text=text)
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
