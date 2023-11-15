from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from django.views import generic
# Create your views here.

from .models import *
from profession.models import *

class CharacterView(generic.ListView):
    template_name = "character/character_list.html"
    context_object_name = "character_list"

    def get_queryset(self):
        return Character.objects.all()


def character_status(request):
    character_status = get_object_or_404(CharacterStatus, character_id=request.POST["character_id"])
    character_growths= get_object_or_404(CharacterGrowths, character_id=request.POST["character_id"])
    profession_list = Profession.objects.all()

    context = {
        "character_status": character_status,
        "character_growths": character_growths,
        "profession_list": profession_list,
    }
    return render(request, "character/character_details.html", context)

