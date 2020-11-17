from django.db import models
from django.utils import timezone
from datetime import datetime

class ArticleCategory(models.Model):
    '''
    Class that implements the associative entity 'ArticleCategory'. Intended to
    keep track of the articles that are assigned to particular categories.
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
            return self.name

class Article(models.Model):
    '''
    Class that implements the strong entity 'Article'. Holds data pertaining
    to an article on the web application.

    # Enum class for Categories - commented out for now, as replaced by ArticleCategory class
    class ArticleCategories(models.TextChoices):
        SPORT = ("SP","Sport")
        POLITICS = ("PO","Politics")
        BUSINESS = ("BU", "Business")
        ENTERTAINMENT = ("EN", "Entertainment")
        SCIENCE_TECHNOLOGY = ("ST", "Science & Technology")
        WORLD_NEWS = ("WN", "World News")

    # fields implementation
    article_categories = models.CharField(max_length=25, choices=ArticleCategories.choices, default=ArticleCategories.SCIENCE_TECHNOLOGY )
    '''
    title = models.CharField(max_length=100, default="ARTICLE TITLE")
    sub_title = models.CharField(max_length=200, default="ARTICLE SUBTITLE") # NEW
    author = models.CharField(max_length=40, default="ARTICLE AUTHOR")
    dop = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
    image_url = models.CharField(max_length=100, default="IMAGE PLACEHOLDER")
    image_caption = models.CharField(max_length=200, default="IMAGE CAPTION") # NEW
    content = models.TextField(default="ARTICLE TEXT CONTENTT")
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(
        ArticleCategory,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='articles', # by calling 'articles' we can fetch all articles in a category
    )

    def __str__(self):
        return self.title

class Comments(models.Model):
    '''
    Class that implements the associative entity 'Comments'. Intended to keep track
    of which User posted what comment_content on which Article. Furthermore a comment foreign key
    may be held in order to discern if a comment is a reply to a parent comment or a general for
    an Article.
    '''
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    comment_content = models.CharField(max_length=300)
    timestamp = models.DateTimeField(verbose_name='Commented On', auto_now=True) # verbose_name acts as a more legible alias for the field name. auto_now means that if the date value is not given upon object creation then if you save said object it will automatically take the current date and time as the value upon Model.save().
    parent_comment = models.ForeignKey('Comments', blank=True, null=True, on_delete=models.CASCADE)

    @property
    def hasParent(self):
        if parent_comment:
            return True
        return False

    def __len__(self):
        return len(self.comment_content)

    def __str__(self):
        output = " '%s', written by: user on article: %s".format(self.comment_content, self.article)
        if(self.hasParent):
            parent = "user"
            output = " '%s', written by: user, reply to: %s".format(self.comment_content, parent)
        return output
