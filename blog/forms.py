from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class MyRegistrationForm(UserCreationForm):
	email=forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'password2')

	def save(self, commit=True):
		user= super(UserCreationForm,self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user