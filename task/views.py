from django.shortcuts import render, redirect
from .models import *

from .forms import *


def get_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    tasks = Task.objects.all()
    form = TaskForm()
    context = {"tasks": tasks, "form": form}

    return render(request, 'task/index.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")

    form = TaskForm(instance=task)
    context = {"form": form}

    return render(request, "task/update_task.html", context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {"task": task}
    return render(request, "task/delete_task.html", context)
