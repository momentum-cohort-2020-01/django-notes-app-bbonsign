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


def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    context = {'id': pk, 'note': note}
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
        return render(request, 'core/note_form.html', context=context)


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NewNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=pk)
    else:
        form = NewNoteForm(instance=note)
        context = {'id': id, 'form': form}
        return render(request, 'core/note_form.html', context=context)


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('/')