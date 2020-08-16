from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns =[
    path('SignUp/',views.SignUp,name='signup'),
    path('Log_In/',views.Log_In,name='login'),
    path('Log_out',views.Log_out,name='logout'),

]
