from django.contrib import admin
from django.urls import path
from django.urls import path

from tasks.views import (
    tasks_view,
    add_task,
    delete_task,
    complete_task,
    completed_tasks_view,
    report_view,
    redirect_to_tasks,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Add all your views here
    path("", redirect_to_tasks),
    path("tasks/", tasks_view),
    path("add-task/", add_task),
    path("delete-task/<int:task_id>/", delete_task),
    path("complete_task/<int:task_id>/", complete_task),
    path("completed_tasks/", completed_tasks_view),
    path("all_tasks/", report_view),
]
