from django.urls import path
from . import views

app_name = "reminder"
urlpatterns = [
  path("", views.index, name="index"),
  path("page/create/", views.create_view, name="page_create"),
  path("page/", views.list_view, name="page_list"),
  path("page/<int:id>/", views.detail_view, name="page_detail"),
  path("page/delete/<int:id>/", views.delete_view, name="page_delete"),
  path("page/update/<int:id>/", views.update_view, name="page_update"),
]
