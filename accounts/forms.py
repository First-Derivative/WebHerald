from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Account

class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

    email = forms.CharField(max_length=50, help_text="Something that looks like username@domain.com",widget=forms.EmailInput(attrs={
    'placeholder': 'jacque@webster.com',
    'class': 'form-control',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'RockstarJeans3500',
    'class': 'form-control',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Password',
    'class': 'form-control mb-4',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirm Password',
    'class': 'form-control mb-4',
    }))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Re-Enter Password"
