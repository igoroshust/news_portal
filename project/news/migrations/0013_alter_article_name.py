# Generated by Django 5.0.3 on 2024-06-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_article_category_alter_article_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=68, unique=True, verbose_name='name'),
        ),
    ]
