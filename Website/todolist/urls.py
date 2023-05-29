from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('todolist', views.todo_list, name='todolist'),
    path('newlist', views.new_list, name='new_list'),
    path('delete/<int:id>/', views.delete_list, name='delete_list'),
    path('updatelist/<int:id>/', views.updatelist, name='updatelist'),
    path('finalizelist/<int:id>/', views.finalizelist, name='finalizelist'),
]
