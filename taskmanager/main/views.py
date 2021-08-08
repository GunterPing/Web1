from django.shortcuts import render
from .models import Task
from django.http import HttpResponse


def index(request):
    tasks=Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Cuka', 'tasks': tasks})
    # return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')
def about2(request):
    return render(request, 'main/about2.html')

def index2(request):
    return render(request, 'main/index2.html')