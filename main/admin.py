from django.contrib import admin
from main.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "timestamp", "image_url", "image_caption")
    search_fields = ("id","author","title")
    readonly_fields = ("timestamp",)

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "article")
    search_fields = ("id","category")

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "article", "content", "parent_comment")
    search_fields = ("id","user", "article")

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory,ArticleCategoryAdmin)
admin.site.register(Likes)
admin.site.register(Comments,CommentsAdmin)
