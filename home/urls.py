from django.urls import path
from . import views

# application namespace
ap_name = 'home' 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]