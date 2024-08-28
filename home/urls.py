from django.urls import path
from . import views

# application namespace
ap_name = 'home' 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('authorized', views.AuthorizedView.as_view(), name='authorized'),
]