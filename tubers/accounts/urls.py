from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logout'), #View cannot be logout. As logout is already pre-defined by django
    path('dashboard', views.dashboard, name='dashboard'),
]