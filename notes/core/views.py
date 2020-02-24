from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World!!!! Again")

def notes_list(request):
    return HttpResponse("Notes List")
