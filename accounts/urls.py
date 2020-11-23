from django.contrib import admin
from django.urls import path
from accounts.views import registerAccount, loginAccount, logoutAccount, getProfilePage

urlpatterns = [
    path('register', registerAccount, name='register'),
    path('login', loginAccount, name='login'),
    path('logout',logoutAccount, name='logout'),
    path('profile', getProfilePage, name='profile')
]
