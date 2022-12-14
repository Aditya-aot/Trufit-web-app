import re
from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages 

from home.models import basic_image

# Create your views here.

def login(request) :
    image = basic_image.objects.all()
    logo_images =  image.filter(name="trufit")
    cart_images =  image.filter(name="cart")

    context={
        'logo_image' : logo_images ,
        'cart_images' : cart_images ,


    }
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username , password=password)

        if user is not None :
            auth.login(request, user)
            return redirect('/')
        
        else :
            messages.info(request, 'invalid credentials')
            return redirect("/accounts/login")
    
    else :
        return render(request, 'accounts/login.html' , context)



def register(request) :

    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2 :
            if User.objects.filter(username=username).exists() :
                messages.info(request,'Username Taken')
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists() :
                messages.info(request,'Email Taken')
                return redirect('/accounts/register')
            else :
                user = User.objects.create_user(username=username, password=password1,email=email, first_name=first_name ,last_name=last_name)
                user.save() ;
                print('user created')
                return redirect('/')
        else:
            messages.info(request, 'password not matching')
            return redirect('/accounts/register')
        return render(request, 'accounts/register.html')


    else :
        print('user not created')
        return render(request, 'accounts/register.html')


def logout(request) :
    auth.logout(request)
    return redirect("/accounts/login")