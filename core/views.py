from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from core.models import *

# 
def index(request):
    pass


def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"This username has taken")
                return redirect()
            elif User.objects.filter(email=email).exists():
                messages.error(request,"This email has taken")
                return redirect()
            else:
                user=User.objects.create_user(
                    username=username,
                    email=email
                )
                user.save()
                user.set_password(password1)

                user_login=authenticate(username=username,password=password1)
                login(request,user_login)

                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect()
        else:
            messages.error(request,"Password must be same")
            return redirect()
    
    else:
        return render(request,"signup.html")
    



def signin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect()
        else:
            messages.error(request,"Wrong Credentials!")
            return redirect()
    
    else:
        return render(request,"")


# 
def signout(request):
    logout(request)
    return redirect()


# 
def upload(request):
    if request.method=="POST":
        user=request.user.username
        image=request.FILES.get("image")
        caption=request.POST.get("caption")

        newpost=Post.objects.create(
            user=user,
            image=image,
            caption=caption
        )
        newpost.save()
        return redirect()
    
    else:
        return redirect()
    

# 
def search():
    pass


# 
def like_post():
    pass


# 
def profile():
    pass


# 
def follow():
    pass


# 
def settings():
    pass


# 

