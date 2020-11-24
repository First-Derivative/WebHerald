from django.shortcuts import render
from .models import CategoryLabel, ArticleCategory, Article
from django.http import HttpResponse

from accounts.models import Account

def index(request):

    '''
    content class is an object, one entry for each category CategoryLabel
    that also keeps tracks of the articles with category == CategoryLabel
    at the appropriate index of content.
    '''

    context = {
        'category_list': ArticleCategory.objects.all(),
        'nav_categories': [category for category in CategoryLabel]
    }
    if(request.user.is_authenticated):
        user = request.user
        user_categories = []
        for category in CategoryLabel:
             if(category in user.get_private_category):
                 user_categories.append(category)
        context['categories'] = user_categories
    else:
        context['categories'] = [category for category in CategoryLabel]
    return render(request, 'main/index.html',context)

def getArticlePage(request, article_id):
    context = {
        'article': Article.objects.get(id=article_id),
        'nav_categories': [category for category in CategoryLabel]

        }
    return render(request, 'main/article.html', context)

def category_index(request, category):
    selected = None

    categories = [category for category in CategoryLabel]

    for categories in CategoryLabel:
        if(categories == category):
            selected = categories
            break

    articles_list = []

    for category_entry in ArticleCategory.objects.all():
        if(category_entry.category_code == selected):
            articles_list.append(category_entry.article)

    print(articles_list)

    context = {
        'selected': selected,
        'articles_list': articles_list,
        'nav_categories': [category for category in CategoryLabel]
    }

    return render(request, 'main/category_index.html', context)
