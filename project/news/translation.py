from .models import *
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', ) # поля для перевода

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('name', 'text', 'category')