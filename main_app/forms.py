from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django import forms

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'

class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=50)

class ProductItemForm(ModelForm):
	class Meta:
		model = ProductItem
		fields = ['quantity', 'price']