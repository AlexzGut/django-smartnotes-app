from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

# Create your views here.
# def index(request):
#     context = { 'today': datetime.today()}
#     return render(request, 'home/index.html', context)

class IndexView(TemplateView):
    template_name = 'home/index.html'
    extra_context = {'today': datetime.today()}

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

# To handle Login in a Class View we must use a mixin - LoginRequiredMixin,
# it must be specified before the generic View in this case Template View
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
