from django import forms


class loginForm(forms.Form):
	"""
	Form for dashboard login
	"""
	username =forms.CharField(max_length=32)
	password =forms.CharField(min_length=3)
