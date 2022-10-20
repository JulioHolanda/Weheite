from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=120, help_text='Required. Enter a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2')
 

class CreateInForum(ModelForm):
    title = forms.CharField(max_length=50, required=True, help_text='Required.')
    body = forms.CharField(max_length=10000, required=True, help_text='Required.')

    class Meta:
        model = Forum
        fields = ['title', 'body']

class CreateInReply(ModelForm):
    body = forms.CharField(max_length=10000, required=True, help_text='Required.')

    class Meta:
        model = Reply
        fields = ['body',]


# class CreateInDiscussion(ModelForm):
#     class Meta:
#         model= Disc
#         fields = "__all__"'''
