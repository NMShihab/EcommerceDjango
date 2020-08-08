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
