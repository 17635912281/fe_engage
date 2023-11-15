from django.urls import path

from . import views

urlpatterns = [
    path("", views.CharacterView.as_view(), name="character_list"),
    path("status/", views.character_status, name="character_status"),
]