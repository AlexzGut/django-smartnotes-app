from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
<<<<<<< HEAD
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
=======
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.edit import DeleteView
>>>>>>> delete-endpoint
from .forms import NotesForm
from .models import Notes

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


# class NewView(TemplateView):
#     template_name = 'notes/new.html'

# def create(request):
#     if ((title := request.POST['title'] == "") and (text := request.POST['text'] == "")):
#         context = {
#             'error_msg': 'all fields are required'
#         }
#         return render(request, 'notes/form.html', context)
#     else:
#         Notes.objects.create(title=title, text=text)
#         return HttpResponseRedirect(reverse('notes:index'))
    
#Django generic CreateView class handles GET and POST requests made to the same url (notes/create)
class CreateNoteView(CreateView):
    # When a POST request is made to notes/create a new Note is created in the database,
    # and the user is redirected to notes/ (notes:index)
    model = Notes
    # Using Django forms
    form_class = NotesForm
    # When a GET request is made to notes/create the user is displayed the notes/new.html template
    # to submit a new POST request to create a Note in the database
    # Used for GET requests to the url notes/create
    template_name = 'notes/form.html' 
    success_url = '/notes'

class UpdateNoteView(UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = 'notes/form.html'
    success_url = '/notes'

class DeleteNoteView(DeleteView):
    model = Notes
    template_name = 'notes/delete_confirmation_form.html'
    success_url = '/notes'