# Generated by Django 5.0.3 on 2024-06-18 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_alter_article_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category_en',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='article',
            name='category_ru',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='article',
            name='name_en',
            field=models.CharField(max_length=68, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='article',
            name='name_ru',
            field=models.CharField(max_length=68, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='article',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='article',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(default=0, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(default=0, max_length=100, null=True, unique=True),
        ),
    ]
