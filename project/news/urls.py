from django.urls import path, include
from .views import (ArticleViewset, CategoryViewset, NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, subscriptions, CategoryListView, subscribe)
from django.views.decorators.cache import cache_page


urlpatterns = [
    # path('', cache_page(60)(NewsList.as_view()), name='news_list'),
    # path('<int:pk>', cache_page(300)(NewsDetail.as_view()), name='news_detail'),
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('search/', NewsSearch.as_view(), name="news_search"),
    path('create/', NewsCreate.as_view(), name='news_create'), # news_edit
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'), # news_update
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]