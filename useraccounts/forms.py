from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(

        attrs={
            "class": "form-group",
            "placeholder": "Leave a Comment!"
        }))