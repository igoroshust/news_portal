# Generated by Django 5.0.3 on 2024-06-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_alter_article_category_alter_article_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]