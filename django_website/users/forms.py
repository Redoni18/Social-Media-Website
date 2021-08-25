from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Chat
import datetime

def last_years():
    first_year = datetime.datetime.now().year - 100
    return list(range(first_year + 101, first_year, -1))

class UserRegister(UserCreationForm):

	email = forms.EmailField()
	class Meta:
		model = User
		labels = {
			"username": "Username",
			"email": "Email",
			"password1":"Password",
			"password2":"Konfirmoni passwordin",
        }
		fields = ['username','email','password1','password2']

class UserUpdate(forms.ModelForm):

	email = forms.EmailField()
	class Meta:
		model = User
		labels = {
			"username": "Username",
			"email": "Email",
        }
		fields = ['username','email']

class ProfileUpdate(forms.ModelForm):
	birth_date = forms.DateTimeField(widget=forms.SelectDateWidget(years = last_years()))
	class Meta:
		model = Profile
		labels = {
			"image":"Profile picture",
        }
		fields = ['Name','Bio','birth_date','statusi','image']
