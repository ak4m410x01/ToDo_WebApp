from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="home"),
    path("<str:slug>/update", views.update, name="update"),
    path("<str:slug>/delete", views.delete, name="delete"),
]
