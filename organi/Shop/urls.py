from django.urls import path
from Shop import  views

app_name = 'Shop'

urlpatterns =[
path('',views.Home.as_view(),name='home')

]
