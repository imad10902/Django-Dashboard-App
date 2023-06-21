from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
    
        user= authenticate(request, username=username, password=password)#authentication step

        if user is not None:
            login(request, user)#this user object is being used in templates
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")
      
    

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def registerPage(request):
    form  = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured')

    context= {'form': form}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect ('home')