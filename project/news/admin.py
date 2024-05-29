from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    """Настройка вывода информации в панели администратора"""
    list_display = ('name', 'date', 'category', )

    list_filter = ('category', )

    search_filter = ('name', 'category__name', )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)