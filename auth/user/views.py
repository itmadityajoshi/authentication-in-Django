from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {
        'form':form
    }
    
    
    return render(request, 'register.html', context)


def login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form  = LoginForm(request, data= request.POST)
        
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            
    context ={
        'loginform':form
    } 
            
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url="login")
def home(request):
    return render(request, 'home.html')