from django.shortcuts import render
from django.http import HttpResponseRedirect

from tasks.models import Task


def pending_tasks():
    return Task.objects.filter(deleted=False).filter(completed=False)


def completed_tasks():
    return Task.objects.filter(deleted=False).filter(completed=True)


def redirect_to_tasks(request):
    return HttpResponseRedirect("/tasks/")


def tasks_view(request):
    return render(
        request,
        "tasks.html",
        {
            "pending_tasks": pending_tasks(),
        },
    )


def completed_tasks_view(request):
    return render(
        request,
        "completed_tasks.html",
        {
            "completed_tasks": completed_tasks(),
        },
    )


def report_view(request):
    return render(
        request,
        "report_view.html",
        {
            "pending_tasks": pending_tasks(),
            "completed_tasks": completed_tasks(),
        },
    )


def add_task(request):
    task_name = request.GET.get("task")
    Task(title=task_name).save()
    print(Task.objects.all())
    return HttpResponseRedirect("/tasks/")


def complete_task(request, task_id):
    Task.objects.filter(id=task_id).update(completed=True)
    return HttpResponseRedirect("/tasks/")


def delete_task(request, task_id):
    Task.objects.filter(id=task_id).update(deleted=True)
    return HttpResponseRedirect("/tasks/")
