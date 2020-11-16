# Generated by Django 3.1.3 on 2020-11-15 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201113_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='ARTICLE AUTHOR', max_length=40),
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='ARTICLE TEXT CONTENTT'),
        ),
        migrations.AddField(
            model_name='article',
            name='dop',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.CharField(default='IMAGE PLACEHOLDER', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_categories',
            field=models.CharField(choices=[('SP', 'Sport'), ('PO', 'Politics'), ('BU', 'Business'), ('EN', 'Entertainment'), ('ST', 'Science & Technology'), ('WN', 'World News')], default='ST', max_length=25),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='ARTICLE TITLE', max_length=100),
        ),
    ]