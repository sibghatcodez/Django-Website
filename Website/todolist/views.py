from django.shortcuts import render, redirect
from .models import List
from datetime import date
from django.contrib.auth.models import User


# Create your views here.
def todo_list(request):
    user = request.user
    all_lists = List.objects.filter(user=user)
    print(all_lists)
    if request.user.is_authenticated:    
        return render(request, 'todolist/todolist.html', {'first_name': user.first_name, 'all_lists': all_lists})

def new_list(request):
    user = request.user
    if request.method == 'POST':
        new_list = request.POST.get('new_list')
        if new_list != '':
            add_list = List(user=user,todo_list=new_list, date=date.today())
            add_list.save()

    # all_lists = List.objects.all()
    all_lists = List.objects.filter(user=user)
    print(all_lists)
    return render(request, 'todolist/todolist.html', {'first_name': user.first_name, 'all_lists': all_lists})

def delete_list(request, id):
    delete_list = List.objects.get(id=id)
    delete_list.delete()
    return redirect('todolist')

def updatelist(request,id):
    list_info = List.objects.get(id=id)
    list = list_info.todo_list
    date = list_info.date
    return render(request, 'todolist/edit.html', {'listID':list_info.id,'list_info':list, 'list_date': date})

def finalizelist(request,id):
    new_list = request.POST.get('updated_list')
    list = List.objects.get(id=id)
    list.todo_list = new_list
    list.save()
    return redirect('todolist')
