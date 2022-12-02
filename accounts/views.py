from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from dashboard.models import Person



def home(request):
    return render(request, 'accounts/home.html')

def account_details(request):
    id = request.user.id
    user = Person.objects.get(user_id = id)
    context = {
        "user" : user
    }
    return render(request, 'accounts/accountdetails.html')    
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'landingpage/loggedin.html')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')



    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            

    else:
        return render(request, 'accounts/registration.html')


def registerdetails(request):
    if request.method == 'POST':
        id = request.POST['user_id']
        user = Person.objects.get(user_id=id)
        user.age = request.POST['age']
        user.gender = request.POST['gender']
        user.height_in = request.POST['height']
        user.weight_lbs = request.POST['weight']

        user.save() 
        return render(request, 'accounts/accountdetails.html')
    else:
        return render(request, 'accounts/registration.html')

def serumdetails(request):
    if request.method == 'POST':
        id = request.POST['user_id']
        user = Person.objects.get(user_id=id)
        user.serum_k_mg_per_dL = request.POST['k']
        user.serum_phos_mg_per_dL_min = request.POST['phos']
        user.serum_na_mEq_per_L_min = request.POST['na']
        user.serum_creatinine_mg_per_dL = request.POST['creatinine']
        user.serum_albumin_mg_per_dL = request.POST['albumin']
        user.serum_blood_sugar_mg_per_dL = request.POST['blood_sugar']

        user.save() 
        return render(request, 'accounts/accountdetails.html')
    else:
        return render(request, 'accounts/registration.html')

def pdetails(request):
    data = Person.objects.all()
    context = {
    }
    return render(request, 'accounts/pdetails.html',context)

def sdetails(request):
    data = Person.objects.all()
    context = {
    }
    return render(request, 'accounts/sdetails.html', context)

def logout_user(request):
    auth.logout(request)
    return render(request, 'accounts/home.html')