# Generated by Django 3.1.2 on 2020-11-17 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201117_1806'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='likes',
            options={'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
    ]