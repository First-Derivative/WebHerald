from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accounts.models import Account
from accounts.forms import RegisterForm

# Create your views here.

def registerAccount(request):
    context = {}

    if(request.POST):
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            # login(request, acccount)
            return redirect('homepage')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)

def loginAccount(request):
    return render(request, 'accounts/login.html')
