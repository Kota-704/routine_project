from django.urls import path
from . import views

app_name = "reminder"
urlpatterns = [
  path("", views.index, name="index"),
  path("page/create/", views.create_view, name="page_create"),
]
