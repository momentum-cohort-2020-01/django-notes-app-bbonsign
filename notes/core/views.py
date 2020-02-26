from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Note
from .forms import NewNoteForm


def index(request):
    return HttpResponse("Hello world")


def note_list(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'core/note_list.html', context=context)


def note_detail(request, id):
    note = Note.objects.get(id=id)
    context = {'id': id, 'note': note}
    return render(request, 'core/note_detail.html', context=context)


def new_note(request):
    if request.method == "POST":
        form = NewNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NewNoteForm()
        context = {'form': form}
        return render(request, 'core/new_note_form.html', context=context)


def edit_note(request, id):
    note = get_object_or_404(Note, pk=id)
    if request.method == "POST":
        form = NewNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', id=id)
    else:
        form = NewNoteForm(instance=note)
        context = {'id': id, 'form': form}
        return render(request, 'core/edit_note.html', context=context)
