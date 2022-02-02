from cProfile import label
from turtle import width
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Shortener

User = get_user_model()


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(label='URL', widget=forms.URLInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Shorten your link'}))

    class Meta:
        model = Shortener
        fields = ('long_url',)


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=100, label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=100, label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        modal = User
        fields = ('username', 'first_name',
                  'last_name', 'email', 'password1', 'password2')
