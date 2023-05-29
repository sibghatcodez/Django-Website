from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo', views.todo, name='todo'),
    path('contact', views.contact, name='contact'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('profile', views.profile, name='profile'),
    path('globalchat', views.globalchat, name='globalchat'),
    ]
