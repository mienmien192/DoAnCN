from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *
from . import models
from .models import Comment


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.video = kwargs.pop('video', None)
        super().__init__( *args, **kwargs)

    def save(self, commit=True):
        cmt=super().save(commit=False)
        cmt.user=self.user
        cmt.video=self.video
        cmt.save()
    class Meta:
        model = Comment
        fields = ["comment"]



class QuestionForm(forms.ModelForm):
    # this will show dropdown __str__ method course model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in course model and return it
    examID = forms.ModelChoiceField(queryset=models.Exam.objects.all(), empty_label="Exam Name",
                                      to_field_name="id")


    class Meta:
        model = models.Question
        fields = ['marks', 'question', 'option1', 'option2', 'option3', 'option4', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }
class Coursesadd(forms.ModelForm):
    class Meta:
        model=Courses
        fields="__all__"
class Studentsadd(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
class Teachersadd(forms.ModelForm):
    class Meta:
        model=Teacher
        fields="__all__"