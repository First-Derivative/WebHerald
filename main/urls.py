from django.contrib import admin
from django.urls import path
from main.views import indexView, articleView, formView

urlpatterns = [
    path('', indexView, name='index'),
    path('/article/', articleView, name='article'),
    path('/user-form/', formView, name='user-form'),
]
