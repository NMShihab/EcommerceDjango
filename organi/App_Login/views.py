from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse


""" Authentication """
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

""" Forms and models """
from App_Login.models import User,UserProfile
from App_Login.forms import ProfileForm, SignUpForm

""" Messages """
from django.contrib import  messages

# Create your views here.

def SignUp(request):
    form = SignUpForm()
    registered = False

    if request.method == "POST":
        form = SignUpForm(data = request.POST)

        if form.is_valid():
            form.save()
            registered = True
            messages.success(request,'Account created successfully')
            return HttpResponseRedirect(reverse('App_Login:login'))

    return render(request,'App_Login/signup.html',context={'form':form,'registered':registered})

def Log_In(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username,password = password)

            if user is not None :
                login(request,user)

                return HttpResponseRedirect(reverse('Shop:home'))


    return render(request,'App_Login/login.html',context={'form':form})


@login_required
def Log_out(request):
    logout(request)
    messages.warning(request,"You are logged out")
    return HttpResponseRedirect(reverse("Shop:home"))

@login_required
def user_profile(request):
    profile = UserProfile.objects.get(user = request.user)

    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST,instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request,"Your profile updated")
            form = ProfileForm(instance=profile)

    return render(request,"App_Login/profilechange.html",context={'form':form})
