from django.contrib import admin
from django.urls import path
from accounts.views import registerAccount, loginAccount

urlpatterns = [
    path('login/', loginAccount, name='login'),
    path('register', registerAccount, name='register'),
]
