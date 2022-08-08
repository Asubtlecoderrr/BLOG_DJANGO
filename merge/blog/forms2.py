
from distutils.command.upload import upload
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from django.conf import settings

User = get_user_model()
# User = settings.AUTH_USER_MODEL

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    image=forms.FileField()
    dob = forms.DateField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self,commit=True):
        user=super(UserRegisterForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name= self.cleaned_data['last_name']
        user.email= self.cleaned_data['email']
        user.image = self.cleaned_data['image']
        user.dob = self.cleaned_data['dob']
        
        if commit:
            user.save()
            
class EditProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','image','dob')
        
        