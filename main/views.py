from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def getArticlePage(request):
    return render(request, 'main/article.html')

def login(request):
    return render(request, 'main/login.html')

def signUp(request):
    return render(request, 'main/sign-up.html')
