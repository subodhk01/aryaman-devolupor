from django.shortcuts import render,redirect    
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            return render(request, 'authentication/login.html', {'error':"Invalid UserName or Password"})
    else:
        return render(request, 'authentication/login.html', {})
@login_required
def logoutView(request):
    logout(request)
    return redirect('/')
