from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from .views import (RegisterView,TaskViewSet,register_page,task_list,task_create,task_update,task_delete,)

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    # HTML pages
    path("", task_list, name="task_list"),
    path("register/", register_page, name="register_page"),
    path(
        "login/",
        LoginView.as_view(template_name="tasks/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(next_page="login"),
        name="logout",
    ),
    path("tasks/create/", task_create, name="task_create"),
    path("tasks/<int:pk>/edit/", task_update, name="task_update"),
    path("tasks/<int:pk>/delete/", task_delete, name="task_delete"),
    path("api/auth/register/", RegisterView.as_view()),
    path("api/", include(router.urls)),
]