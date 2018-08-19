from django.forms import modelform_factory
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from todo_list.models import Todo
from todo_list.serializers import TodoSerializer


def index(request):
    TodoForm = modelform_factory(Todo, fields=('__all__'))
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tdd_todo_list/')
    else:
        form = TodoForm()
        todo_list = Todo.objects.all()
    return render(request, 'todo_list/index.html', {'form': form, 'todo_list': todo_list})


@csrf_exempt
def todo_list(request):
    """
    List all code todos, or create a new todo.
    """
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def todo_detail(request, pk):
    """
    Retrieve, update or delete a code todo.
    """
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=204)
