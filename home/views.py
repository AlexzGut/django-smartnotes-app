from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = '/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes:index')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        if the form is valid, authenticate the user and
        redirect to the supplied URL.
        """
        self.object = form.save()
        login(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())
