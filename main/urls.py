from django.contrib import admin
from django.urls import path
from main.views import index, getArticlePage, login, signUp

urlpatterns = [
    path('', index, name='index'),
    path('article/<int:article_id>', getArticlePage, name='article'),
    path('login/', login, name='login'),
    path('sign-up/', signUp, name='sign-up'),
]
