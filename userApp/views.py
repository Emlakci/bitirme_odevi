from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from userApp.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

#~ Function that check if password typed by user is suitable
def checkPassIsSuitable(password):
    include_number = False
    include_upperChar = False
    for char in password:
        if char.isnumeric(): include_number = True
        if char.isupper(): include_upperChar = True 

    if len(password)>=8 and include_number and include_upperChar :
        return True
    else :
        return False
#~ Function that check if password typed by user is suitable

def loginPage(request):
    context ={}
    return render(request,'loginPage.html', context)

def registerPage(request):
    context ={}
    return render(request,'registerPage.html', context)

@login_required(login_url='loginPage')
def accountPage(request):
    context ={}
    return render(request,'accountPage.html', context)

@login_required(login_url='loginPage')
def user_logout(request):
    logout(request)
    return redirect('homePage')