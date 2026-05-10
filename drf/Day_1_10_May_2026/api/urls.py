from django.urls import path
from .views import NoteAPIView

urlpatterns = [
    path('notes/' , NoteAPIView.as_view()),
    path('notes/{pk}' , NoteAPIView.as_view()),
]