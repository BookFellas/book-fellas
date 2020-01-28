from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'