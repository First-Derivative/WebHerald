from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.exceptions import SuspiciousOperation

from accounts.models import Account
from main.models import CategoryLabel

from accounts.forms import RegisterForm, LoginForm

def registerAccount(request):
    context = {}
    if(request.user.is_authenticated):
        return redirect('homepage')

    if(request.POST):
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('homepage')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)


def loginAccount(request):
    context = {}

    if(request.user.is_authenticated):
        return redirect('homepage')

    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if(user):
                login(request, user)
                return redirect("homepage")
    else:
        form = LoginForm()
        context['login_form'] = form
    return render(request, 'accounts/login.html', context)

def logoutAccount(request):
    logout(request)
    return redirect('homepage')

@login_required
def getProfilePage(request):
    user = request.user
    context = {
        'categories': [category for category in CategoryLabel],
        'personal_categories': user.get_private_category
    }
    return render(request, 'accounts/profile.html',context)

@login_required
def modify_personal_category(request):
    user = request.user
    if(request.POST):
        if(request.POST.get('operation') == 'add'):
            try:
                content = request.POST.get('content')
                user.add_category(content)
            except SuspiciousOperation:
                # http response conflict
                HttpResponse(status=409)
        else:
            try:
                content = request.POST.get('content')
                user.remove_category(content)
            except SuspiciousOperation:
                # http response conflict
                HttpResponse(status=409)
        # http response ok
        return HttpResponse(status=200)
    else:
        return redirect('homepage')
