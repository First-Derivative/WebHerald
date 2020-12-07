from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


from accounts.models import Account

class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email", "username", "dob", "password1", "password2")

    email = forms.CharField(max_length=50, help_text="This is what you'll use to login",widget=forms.EmailInput(attrs={
    'placeholder': 'jacque@webster.com',
    'class': 'form-control ',
    }))

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
    'placeholder': 'RockstarJeans3500',
    'class': 'form-control ',
    }))

    dob = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={
    'type': 'date',
    'placeholder': '1999-09-09',
    'class': 'form-control ',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Password',
    'class': 'form-control ',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirm Password',
    'class': 'form-control ',
    }))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Re-Enter Password"

class LoginForm(ModelForm):

    email = forms.CharField(max_length=50,widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Incorrect Credentials")


class ImageForm(ModelForm):
    class Meta:
        model = Account
        fields = ('profile_pic',)
        '''
        widgets = {'profile_pic':forms.FileInput(
            attrs={'style':'display: none;','class':'form-control', 'required': False, }
             )}
        '''
