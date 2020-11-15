from django.contrib import admin
from django.urls import path
from main.views import indexView

urlpatterns = [
    path('', indexView),
]
