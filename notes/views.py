from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from .models import Notes

# Create your views here.

# def index(request):
#     note_list = Notes.objects.all()
#     context = { 'notes': note_list}
#     return render(request, 'notes/index.html', context)

# IndexView is a subclass of generic.ListView,
# it is performing the same task as the index function() specified above.
class IndexView(ListView):
    # By default Django will look for a template called -> <app name>/<model name>_list.html
    # We are using the attribute template_name to override the template name Django should look for
    template_name = 'notes/index.html'
    context_object_name = 'notes'

    # Using type hint for code readability
    def get_queryset(self) -> QuerySet[Notes]:
        return Notes.objects.all()
    
# pk is the parameter url specified in urls.py
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist in the database')

#     context = { 'note': note }
#     return render(request, 'notes/detail.html', context)


# DetailView will handle a Notes.DoesNotExist,
# redirecting the user to the 404 Page Not Found and displaying an appropiate message
class DetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/detail.html'
