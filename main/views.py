from django.shortcuts import render

# Create your views here.

# Serve up the homepage
def indexView(request):
    return render(request, 'main/index.html')

# Serve article page, hardcoded for now
def articleView(request):
    return render(request, 'main/article.html')
