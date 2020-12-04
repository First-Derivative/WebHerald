from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from accounts.models import Account

def index(request):

    '''
    content class is an object, one entry for each category CategoryLabel
    that also keeps tracks of the articles with category == CategoryLabel
    at the appropriate index of content.
    '''

    context = {
        'category_list': ArticleCategory.objects.order_by('-article_id'),
        'nav_categories': [category for category in CategoryLabel],
        'test': []
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
    article = Article.objects.get(id=article_id)
    selected_category = ArticleCategory.objects.get(article=article)
    comments = Comments.objects.filter(article=article)
    comments = comments.filter(parent_comment=None)

    context = {
        'article': article,
        'article_comments': comments,
        'selected_category': selected_category,
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
    context = {
        'selected': selected,
        'articles_list': articles_list,
        'nav_categories': [category for category in CategoryLabel]
    }

    return render(request, 'main/category_index.html', context)


@login_required
def updateLikes(request, article_id):
    try:
        # get article and user
        article = Article.objects.get(id=article_id)
        user = request.user

        # determine whether user already likes article
        if request.method == 'GET':
            if Likes.objects.filter(article=article, user=user).exists():
                return JsonResponse({'is_liked': 'true'})
            else:
                return JsonResponse({'is_liked': 'false'})

        # Add like
        if request.method == 'POST':
            Likes.objects.create(article=article, user=user)
            likes = article.like_count
            return JsonResponse({'num_likes': likes})

        # Remove like
        if request.method == 'DELETE':
            current_like = Likes.objects.filter(article=article, user=user)
            current_like.delete()
            likes = article.like_count
            return JsonResponse({'num_likes': likes})

    except Article.DoesNotExist:
        return HttpResponseBadRequest("Invalid Article ID")

@login_required
def addComment(request):
    if(request.method == 'POST'):
        post = request.POST
        state = post.get('state')
        if(state == 'new_comment'):
            post_article = post.get('article')
            article = None
            content = post.get('content')
            user = request.user

            # verifying article
            try:
                article = Article.objects.get(id=post_article)
            except Article.DoesNotExist:
                return HttpResponseBadRequest("Invalid Article ID")

            new_comment = Comments(article=article, user=user, content=content)
            new_comment.save()
            return JsonResponse({'comment': new_comment.id})
        elif(state == 'reply'):
            post_user = post.get('user')
            return HttpResponse(status=200)
        return HttpResponseBadRequest("Suspicious Request")
    return redirect('homepage')

@login_required
def removeComment(request, comment_id):
    if(request.method == 'DELETE'):
        comment = None
        user = request.user

        #verify comment
        try:
            comment = Comments.objects.get(id=comment_id)
        except Comments.DoesNotExist:
            return HttpResponseBadRequest("Invalid Comment ID")

        #verify user
        if(comment.user == user):
            comment.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponseBadRequest("Suspicious Request")
    return redirect('homepage')
