from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from userApp.models import *
from mainApp.message import messages
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

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user: #authentication successful
                message = {
                    'message' : messages.get('auth_success'),
                }

                try:
                    # Is there a CustomUser object for the user?
                    custom_user = CustomUser.objects.get(user=user)

                except CustomUser.DoesNotExist: 
                    # If a CustomUser object is not found for the user
                    # join tables User & CustomUser
                    custom_user = CustomUser(user=user)
                    custom_user.save()
                
                #login process continue
                login(request, user)

                return JsonResponse(message, status=200)
            
            else: # parameters did not match
                message = {
                    'message' : messages.get('auth_failure')
                }

                return JsonResponse(message, status=401)

        else: # for null inputs 
            message = {
                'message' : messages.get('null_values')
            }

            return JsonResponse(message, status=400)
        
    return render(request,'loginPage.html', context)

def registerPage(request):
    context ={}

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 =request.POST.get('password2')

        if firstname and lastname and username and email and password1:
            if password1 == password2:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        ##check pass is suitable
                        if checkPassIsSuitable(password1):
                            ## pass is ok
                            message = {
                                'message' : messages.get('register_success')
                            }
                            ## record user to DB
                            newUser = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password1)
                            newUser.save()

                            return JsonResponse(message, status=202)
                        
                        else:
                            message = {
                                'message' : messages.get('pass_format_failure')
                            }

                            return JsonResponse(message, status=203) 
                    else:
                        message = {
                            'message' : messages.get('existed_email')
                        }
                        return JsonResponse(message, status=203) 
                else:
                    message = {
                                'message' : messages.get('existed_user')
                    }

                    return JsonResponse(message, status=203)    
            else:
                message = {
                    'message' : messages.get('check_pass_failure')
                }

                return JsonResponse(message, status=401)
        else:
            message = {
                'message' : messages.get('null_values')
            }

            return JsonResponse(message, status=400)

    return render(request,'registerPage.html', context)

@login_required(login_url='loginPage')
def accountPage(request):
    context ={}
    
    return render(request,'accountPage.html', context)

@login_required(login_url='loginPage')
def user_logout(request):
    logout(request)
    return redirect('homePage')