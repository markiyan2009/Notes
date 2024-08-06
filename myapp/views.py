from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from myapp.models import Note
from myapp import forms
from django.urls import reverse_lazy
# Create your views here.

class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'

class CreateNoteView(CreateView):
    model = Note
    template_name = 'notes/add_note.html'
    form_class = forms.CreateNoteForm
    success_url = reverse_lazy('myapp:notes-list')