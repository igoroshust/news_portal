# Generated by Django 5.0.3 on 2024-04-06 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-date',), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
