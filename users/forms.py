from django import forms
from .models import Post
from posts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website',)

		
class CreatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']