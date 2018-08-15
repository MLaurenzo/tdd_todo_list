from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome on the todo list application !")
