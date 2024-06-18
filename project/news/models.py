from django.db import models
from django.urls import reverse
from datetime import datetime, timezone
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.core.cache import cache
from django.utils.translation import gettext as _


class Category(models.Model):
    """Категория статей"""
    name = models.CharField(max_length=100)
    subscribers = models.ManyToManyField(User, related_name='categories')

    class Meta:
        # ordering = ('-date',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name.title()

class Article(models.Model):
    """Статья"""
    name = models.CharField(max_length=68, unique=True, verbose_name=_('Name'))
    text = models.TextField(verbose_name=_('Text'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('Date'))
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.CASCADE, verbose_name=_('Category'))

    # def get_absolute_url(self):
    #     """Отображение конкретной страницы после создания товара"""
    #     return reverse('news_detail', args=[str(self.id)])

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def save(self, *args, **kwargs):
        """Низкоуровневое кэширование"""
        super().save(*args, **kwargs) # вызываем метод родителя для сохранения объекта
        cache.delete(f'product-{self.pk}') # удаляем объект для сброса кэша

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class ArticleCategory(models.Model):
    """Промежуточная таблица для связи Article-Category"""
    articleThrough = models.ForeignKey(Article, on_delete=models.CASCADE) # связь «один ко многим» с моделью Post
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE) # связь «один ко многим» с моделью Category

class Subscriber(models.Model):
    """Список категорий, на которые подписан пользователь"""
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )