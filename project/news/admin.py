from django.contrib import admin
from .models import Article, Category
from modeltranslation.admin import TranslationAdmin # импортируем модель админки

class CatAdmin(TranslationAdmin):
    model = Category


class ArticleAdmin(admin.ModelAdmin):
    """Настройка вывода информации в панели администратора"""
    list_display = ('name', 'date', 'category', )

    list_filter = ('category', )

    search_filter = ('name', 'category__name', )

class ArtAdmin(ArticleAdmin, TranslationAdmin):
    model = Article

admin.site.register(Article, ArtAdmin)
admin.site.register(Category)