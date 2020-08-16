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
            return HttpResponseRedirect(reverse('App_Login:login'))

    return render(request,'App_Login/signup.html',context={'form':form,'registered':registered})

def Log_In(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            username = form.cleaned_data("username")
            password = form.cleaned_data("password")

            user = authenticate(username=username,password = password)

            if user is not None :
                login(request,user)

                return HttpResponseRedirect(reverse())


    return render(request,'App_Login/login.html',context={'form':form})


@login_required
def Log_out(request):
    logout(request)
    pass
