from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.core.exceptions import SuspiciousOperation

from accounts.models import Account
from main.models import CategoryLabel

from accounts.forms import RegisterForm, LoginForm, ImageForm

def registerAccount(request):
    context = {
        'nav_categories': [category for category in CategoryLabel]
    }
    if(request.user.is_authenticated):
        return redirect('homepage')

    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)

            # send welcome email
            template = render_to_string('accounts/email.html', {'name' : request.user.username})
            email = EmailMessage(
                'Thank you for signing up to WebHerald',
                template,
                settings.EMAIL_HOST_USER,
                [request.user.email],
            )
            email.fail_silently = False
            email.send()

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
            messages.info(request, 'Email or password is incorrect, please try again')
            return redirect("login")
    else:
        form = LoginForm()
        context['login_form'] = form
        context['nav_categories'] = [category for category in CategoryLabel]
    return render(request, 'accounts/login.html', context)

def logoutAccount(request):
    logout(request)
    return redirect('homepage')

@login_required
def getProfilePage(request):
    user = request.user
    form = ImageForm()
    default = user._meta.get_field('profile_pic').get_default()

    # Handle image form, case = update image
    if(request.method == 'POST' and 'update' in request.POST):
        try:
            form = ImageForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
        except ValidationError:
            # unprocessible entity
            HttpResponse(status=409)

    # On 'delete' replace with default profile image
    if(request.method == 'POST' and 'delete' in request.POST):
        user.profile_pic = default
        user.save()

    context = {
        'image_form': form,
        'nav_categories': [category for category in CategoryLabel],
        'categories': [category for category in CategoryLabel],
        'personal_categories': user.get_private_category
    }
    return render(request, 'accounts/profile.html',context)

@login_required
def modify_personal_category(request):
    user = request.user
    if(request.method == 'POST'):
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
