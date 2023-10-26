from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ToDo

def home(request):
    todos = ToDo.objects.all()
    context = {
        'todos':todos
    }
    return render(request, 'todo_app/home.html', context)


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = ToDo(title=title)
    todo.save()
    return redirect('home')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('home')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')