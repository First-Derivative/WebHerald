from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [

    path('register', registerAccount, name='register'),
    path('login', loginAccount, name='login'),
    path('logout',logoutAccount, name='logout'),
    path('profile', getProfilePage, name='profile'),

    path('api/private_categories/modify', modify_personal_category, name="modify_personal_category")
]
