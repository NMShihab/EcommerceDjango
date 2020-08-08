from App_Login.models import User, UserProfile
from django.forms import  ModelForm

from django.contrib.auth.forms import UserCreationForm

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2',)    
        
