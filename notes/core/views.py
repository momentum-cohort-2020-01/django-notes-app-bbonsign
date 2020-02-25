from django.shortcuts import render

from data import NOTES
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world")


def notes_list(request):
    return render(request, 'base.html', context={'notes': NOTES})
