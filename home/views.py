from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime

# Create your views here.
# def index(request):
#     context = { 'today': datetime.today()}
#     return render(request, 'home/index.html', context)

class IndexView(TemplateView):
    template_name = 'home/index.html'
    extra_context = {'today': datetime.today()}

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
