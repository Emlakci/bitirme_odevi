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
    context = {}
    user = request.user
    #get authenticated user
    if request.user.is_authenticated:
        try:
            custom_user = user.customuser
            user_age = custom_user.calculate_age()

            context['auth_user'] = user
            context['auth_user_age'] = user_age
        except:
            print('error')
            pass
    
    #get changing form values
    if request.method == 'POST':
        print(request.POST)
        changingInpName = request.POST.get('hidden_name')
        changing_value = request.POST.get('changing_value')
        
         # if profile img was posted as value  
        if changingInpName == 'profile_img':
            changing_value = request.FILES['changing_value']
        
        password = request.POST.get('control_pass')
        
        # get second inp_value for changing password process
        changing_value_2 = request.POST.get('changing_value_2') if 'changing_value_2' in request.POST else None

        # control pass for accept changing process
        if changing_value and password:
            # check if user password is matched
            if check_password(password,user.password):
                print('accepted')

                if changingInpName == 'first_name' or changingInpName == 'last_name' or changingInpName == 'username' or changingInpName == 'email':
                    setattr(user, changingInpName, changing_value)
                    user.save()
                    print(getattr(user, changingInpName))

                    message = {
                        'message' : messages.get('changing_success')
                    }

                    return JsonResponse(message, status=200) 
                   
                if changingInpName == 'birth_date' or changingInpName == 'city' or changingInpName == 'profile_img':
                    setattr(user.customuser, changingInpName, changing_value)
                    user.customuser.save()
                    print(getattr(user.customuser, changingInpName))

                    message = {
                        'message' : messages.get('changing_success')
                    }
                    
                    return JsonResponse(message, status=200)
              
                if changingInpName == 'password':
                    if changing_value_2 :
                        # check if passwords typed by the user are equal
                        if changing_value == changing_value_2 :
                            # control the password for right pattern
                            if checkPassIsSuitable(changing_value):
                                user.set_password(changing_value)
                                user.save()
                                print(getattr(user, changingInpName))
                                message = {
                                    'message' : messages.get('changing_success')
                                }
                    
                                return JsonResponse(message, status=200)
                            
                            else: #pass is not suitable
                                print('process failed', 'Sifre kriterlere uygun degil!')
                                message = {
                                    'message': messages.get('pass_format_failure')
                                }
                                return JsonResponse(message, status=406)
                        else: # given pass didn't matched
                            print('process failed', 'Sifreler eslesmedi!')
                            message = {
                                'message': messages.get('pass_match_failure')
                            }
                            return JsonResponse(message, status=406)
                    else: # user didn't rewrite the password wanted to update     
                        print('process failed', 'Tekrar sifre alani bos!')
                        message = {
                            'message': messages.get('null_values')
                            }
                        return JsonResponse(message, status=406)
            else :
                print('passwords did not matched!')
                message = {
                    'message': messages.get('check_pass_failure')
                }
                return JsonResponse(message, status=406)
        else:
            print('null values can not be accepted!')
            message = {
                'message' : messages.get('null_values')
                }
            return JsonResponse(message, status=406)

    else:
        return render(request,'accountPage.html', context)

@login_required(login_url='loginPage')
def user_logout(request):
    logout(request)
    return redirect('homePage')