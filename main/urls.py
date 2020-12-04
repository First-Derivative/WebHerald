from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('category/<str:category>', category_index, name='category_index'),
    path('article/<int:article_id>', getArticlePage, name='article'),
    path('api/likes/<int:article_id>', updateLikes, name='likes'),
    path('api/comments/add', addComment, name='addComment'),
    path('api/comments/<int:comment_id>/remove', removeComment, name='removeComment')
]
