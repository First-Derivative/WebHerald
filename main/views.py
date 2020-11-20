from django.shortcuts import render
from .models import CategoryLabel, ArticleCategory, Article

def index(request):

    '''
    content class is an object, one entry for each category CategoryLabel
    that also keeps tracks of the articles with category == CategoryLabel
    at the appropriate index of content.
    '''

    labels = []

    for category in CategoryLabel:
        labels.append(category)

    context = {
        'categorylabels': labels,
        'category_list': ArticleCategory.objects.all()
    }

    return render(request, 'main/index.html',context)

def getArticlePage(request, article_id):
    context = {
        'article': Article.objects.get(id=article_id),
        }
    return render(request, 'main/article.html', context)
