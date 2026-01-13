from django.shortcuts import render, redirect
from .models import Task

def home(request):
    if request.method == "POST":
        task_name = request.POST.get("task")
        task_desc = request.POST.get("description")  # Description from form
        if task_name:
            Task.objects.create(name=task_name, description=task_desc)
        return redirect("/")  # Redirect to home page

    tasks = Task.objects.all()
    return render(request, "todoapp/home.html", {"tasks": tasks})
