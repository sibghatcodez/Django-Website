from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import GlobalChat

# Create your views here.
def home(request):
    gc = GlobalChat.objects.values_list('user', 'msg')
    return render(request, 'login/index.html', {'gc': gc})


def globalchat(request):
    user = request.user
    msg = request.POST.get('gc_msg')
    addMsg = GlobalChat(user=user, msg=msg)
    addMsg.save()
    gc = GlobalChat.objects.values_list('user', 'msg')
    return render(request, 'login/index.html', {'gc': gc})


def profile(request):
    user = request.user
    params = {'username': user.username,
              'first_name': user.first_name,
              'last_name': user.last_name,
              'email': user.email}
    return render(request, 'login/profile.html',params)

def signup(request):
        if request.method == "POST":
              username = request.POST['username']
              firstname = request.POST['firstname']
              lastname = request.POST['lastname']
              email = request.POST['email']
              password = request.POST['password']
              myuser = User.objects.create_user(username, email, password)
              myuser.first_name = firstname
              myuser.last_name = lastname
              myuser.save()
              login(request, myuser)
              messages.success(request,'Your account was successfully registered!')
            #   params = {'firstname':myuser.first_name}
            #   return render(request, 'login/index.html', params)
              gc = GlobalChat.objects.values_list('user', 'msg')
              return render(request, 'login/index.html', {'gc': gc})
        
        return render(request, "login/signup.html")

def contact(request):
    # return render(request, 'login/index.html')
    pass

def todo(request):
    # return render(request, 'login/index.html')
    pass


def signin(request):
                
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                  login(request, user)
                  gc = GlobalChat.objects.values_list('user', 'msg')
                  return render(request, 'login/index.html', {'gc': gc})
                  # params = {'firstname':user.first_name}
                  # return render(request, 'login/index.html', params)
            else:
                  messages.error(request, "Wrong Credentials!")
                  return redirect('home')

        return render(request, 'login/signin.html')


def signout(request):
    logout(request)
    messages.success(request,"Successfully logged-out!")
    return redirect('home')

