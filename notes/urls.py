from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.UpdateNoteView.as_view(), name='edit'),
    path('create', views.CreateNoteView.as_view(), name='create'),
]