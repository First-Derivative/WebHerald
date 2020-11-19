from django.shortcuts import render
from .models import ArticleCategory, Article

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {
        'categories' : ArticleCategory.objects.all(),
    })

def getArticlePage(request, article_id):
    context = {
        'article': Article.objects.get(id=article_id),
        }
    return render(request, 'main/article.html', context)
