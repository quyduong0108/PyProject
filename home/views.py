from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from django.http import HttpResponseRedirect
from .forms import RegistrationForm
# Create your views here.
def index(request): 
  return render(request,'page/home.html')
def contact(request): 
   return render(request,'page/contact.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'page/register.html', {'form': form})
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect  # Add this import statement

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, 'page/login.html')

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect('/login')  # Add the missing parenthesis
