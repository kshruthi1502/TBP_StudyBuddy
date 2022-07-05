from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import Course


        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class EnrollForm(forms.ModelForm):
        class Meta:
            model = Course
            fields = ['user','coursename']

# class StudentForm(forms.ModelForm):
#         class Meta:
#             model = Student
#             fields = ['review','label']



    
   