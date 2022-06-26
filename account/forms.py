from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	def clean_email(self):
		email = self.cleaned_data['email']
		user = User.objects.filter(email=email).exists()
		if user:
			raise ValidationError('already used!!')
		return email

	def clean(self):
		clean_data = super().clean()
		password1 = clean_data.get('password1')
		password2 = clean_data.get('password2')

		if password2 and password1 and password1 != password2:
			raise ValidationError("pass didn't match")


class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
