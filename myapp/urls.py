from django.urls import path
from myapp import views
urlpatterns = [
    path("",views.NoteListView.as_view(), name='notes-list'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name="note-detail"),
    path("create-note", views.CreateNoteView.as_view(), name='add-note')
]