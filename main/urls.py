from django.contrib import admin
from django.urls import path
from main.views import index, getArticlePage

urlpatterns = [
    path('', index, name='homepage'),
    path('article/<int:article_id>', getArticlePage, name='article'),
]
