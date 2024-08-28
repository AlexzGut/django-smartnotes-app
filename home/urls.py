from django.urls import path
from . import views

# application namespace
ap_name = 'home' 
urlpatterns = [
    path('', views.index, name='index'),
    path('authorized', views.authorized, name='authorized'),
]