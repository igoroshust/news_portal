from django.contrib import admin
from .models import Article, Category
from modeltranslation.admin import TranslationAdmin # импортируем модель админки

class CatAdmin(TranslationAdmin):
    model = Category

class ArtAdmin(TranslationAdmin):
    model = Article

class ArticleAdmin(admin.ModelAdmin):
    """Настройка вывода информации в панели администратора"""
    list_display = ('name', 'date', 'category', )

    list_filter = ('category', )

    search_filter = ('name', 'category__name', )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)