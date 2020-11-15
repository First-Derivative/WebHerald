from django.contrib import admin
from django.urls import path
from main.views import indexView, articleView

urlpatterns = [
    path('', indexView, name='index'),
    path('/article/',  articleView, name='article'),
]
