from django import forms
from yarp.models import Post


class loginForm(forms.Form):
	"""
	Form for dashboard login
	"""
	username =forms.CharField(max_length=32)
	password =forms.CharField(min_length=3)


class AddPostForm(forms.ModelForm):
	"""
	Form for saving posts
	"""
	class Meta:
		model = Post
		fields = ['owner', 'title', 'body', 'is_published', 'attachment']