from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


""" Authentication """
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

""" Forms and models """
from App_Login.models import User,UserProfile
from App_Login.forms import ProfileForm, SignUpForm

# Create your views here.

def SignUp(request):
    form = SignUpForm()
    registered = False

    if request.method == "POST":
        form = SignUpForm(data = request.POST)

        if form.is_valid():
            form.save()
            registered = True
    
    return render(request,'App_Login/signup.html',context={'form':form,'registered':registered})

