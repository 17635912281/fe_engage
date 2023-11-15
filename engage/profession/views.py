from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def profession_list(request):
    return HttpResponse("profession_list")


def profession_growths(request):
    return HttpResponse("profession_growths")
