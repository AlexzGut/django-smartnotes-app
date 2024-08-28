from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def index(request):
    context = { 'today': datetime.today()}

    return render(request, 'home/index.html', context)

@login_required(login_url="/admin")
def authorized(request):
    return render(request, 'home/authorized.html', {})
