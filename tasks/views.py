from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskFrom

# Create your views here.


def index(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        form = TaskFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TaskFrom()

    context = {
        "tasks": tasks,
        "form": form,
    }
    return render(request, "list.html", context)


def update(request, slug):
    task = Task.objects.get(slug=slug)

    if request.method == "POST":
        form = TaskFrom(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskFrom(instance=task)

    context = {
        "task": task,
        "form": form,
    }
    return render(request, "update.html", context)
