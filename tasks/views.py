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
