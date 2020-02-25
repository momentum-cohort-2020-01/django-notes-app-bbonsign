from django.shortcuts import render
from django.http import HttpResponse

from .models import Note


def index(request):
    return HttpResponse("Hello world")


def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/note_list.html', context={'notes': notes})


def note_detail(request, id):
    note = Note.objects.get(id=id)
    return render(request, 'core/note_detail.html', context={'id': id, 'note': note})
