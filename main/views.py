from django.shortcuts import render
from .models import CategoryLabel, ArticleCategory, Article

from accounts.models import Account
from django.contrib.auth.models import AnonymousUser

def index(request):

    '''
    content class is an object, one entry for each category CategoryLabel
    that also keeps tracks of the articles with category == CategoryLabel
    at the appropriate index of content.
    '''

    context = {
        'category_list': ArticleCategory.objects.all()
    }
    if(request.user.is_authenticated):
        user = request.user
        user_categories = []
        for category in CategoryLabel:
             if(category in user.get_private_category):
                 user_categories.append(category)
        context['categorylabels'] = user_categories
    else:
        context['categorylabels'] = [category for category in CategoryLabel]
    return render(request, 'main/index.html',context)

def getArticlePage(request, article_id):
    context = {
        'article': Article.objects.get(id=article_id),
        }
    return render(request, 'main/article.html', context)
