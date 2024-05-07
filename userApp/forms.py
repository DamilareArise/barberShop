from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class Admin_form(forms.ModelForm):

    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]

    displayPicture = forms.ImageField(required=False, label='Profile Picture')
    portfolio = forms.FileField(required=False, label='Portfolio')
    gender = forms.ChoiceField(choices =genders, required=False, widget= forms.RadioSelect)
    class Meta:
        model = UserProfile
        fields = [
            'phone_number',
            'address',
            'gender',
            'date_of_birth',
            'portfolio',
            'nationality',
            'displayPicture',
            'department',
            'staff',
            'HOD'
        ]


        widgets = {
            'date_of_birth': forms.NumberInput(attrs={'type':'date'}),
        }


class UserProfileForm(forms.ModelForm):
    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]

    displayPicture = forms.ImageField(required=False, label='Profile Picture')
    gender = forms.ChoiceField(choices =genders, required=False, widget= forms.RadioSelect)
    class Meta:
        model = UserProfile
        fields = [
            'phone_number',
            'address',
            'gender',
            'date_of_birth',
            'nationality',
            'displayPicture',
         ]
        
        widgets = {
            'date_of_birth': forms.NumberInput(attrs={'type':'date'}),
        }