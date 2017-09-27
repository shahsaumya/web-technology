from app.models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea

class UserForm(forms.ModelForm):
  password = forms.CharField (widget=forms.PasswordInput(attrs={'class': "input-lg", 'size':"40"}))
  first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),
  )
  last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),
  )
  username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),
  )
  email = forms.CharField(
        widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),
  )

  #last_name = forms.CharField(
   #     widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),
   # )
  #username = forms.CharField(
   #     widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),
   # )
  #email = forms.CharField(
   #     widget=forms.TextInput(attrs={'class': "input-lg", 'size':"40"}),
   # )

  class Meta:
    model = User
    fields = ('first_name','last_name','username','email','password')
    labels = {
                          'first_name' :('First Name'),
                          'last_name' :('Last Name'),
                          'Username' :('Username'),
                          'email' :('E-mail ID'),
                          'password' :('Password'),
                        }

class UserProfileForm(forms.ModelForm):

  age = forms.CharField(
        widget = forms.TextInput(attrs={'class':"input-lg",'size':"40"}),
  )

  class Meta:
      model = UserProfile
      fields = ('age',)
      labels = {
                 'age' :('Age'),
               }