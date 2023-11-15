from django.urls import path

from . import views

urlpatterns = [
    path("", views.profession_list, name="profession_list"),
    path("growths/", views.profession_growths, name="profession_growths"),
]