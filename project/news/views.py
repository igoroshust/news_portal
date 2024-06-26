import json

import django_filters
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import *
from .forms import NewsForm
from .filters import NewsFilter
from django.urls import reverse_lazy
from datetime import datetime
from pprint import pprint
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Exists, OuterRef
from django.views.decorators.csrf import csrf_protect
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.translation import gettext as _
from django.utils.translation import activate, get_supported_language_variant
import pytz # модуль для работы с часовыми поясами

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import *

# def articles(request):
#     if request.method == 'GET':
#         return HttpResponse(json.dumps([
#             {
#                 "id":article.id,
#                 "name":article.name,
#                 "text":article.text,
#             } for art in Article.objects.all()
#         ]))
#     if request.method == 'POST':
#         # Нужно извлечь параметы из тела запроса
#         json_params = json.loads(request.body)
#
#         articles = Article.objects.create(
#             name=json_params['name'],
#             address=json_params['text']
#         )
#         return HttpResponse(json.dumps({
#             "id":article.id,
#             "name":article.name,
#             "text":article.text,
#         }))
#
# def article_id(request, article_id):
#     article = Article.objects.get(id=article_id)
#     if request.method == 'GET':
#         return HttpResponse(json.dumps(
#              {
#                 "id":article.id,
#                 "address":article.address,
#                 "name":article.name
#             }))
#     json_params = json.loads(request.body)
#     if request.method == 'PUT':
#         article.address = json_params['address']
#         article.name = json_params['name']
#         article.save()
#         return HttpResponse(json.dumps({
#             "id":article.id,
#             "name":article.name,
#             "text":article.text,
#         }))
#     if request.method == 'PATCH':
#         article.address = json_params.get('text',article.text)
#         article.name = json_params.get('name',article.name)
#         article.save()
#         return HttpResponse(json.dumps({
#             "id":article.id,
#             "name":article.name,
#             "text":article.name,
#         }))
#     if request.method == 'DELETE':
#         article.delete();
#         return HttpResponse(json.dumps({}))

class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all().filter(is_active=True)
    serializer_class = ArticleSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def list(self, request, format=None):
    #     return Response([])

    # def destroy(self, request, pk, format=None):
    #     instance = self.get_object()
    #     instance.is_active = False
    #     instance.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = Article.objects.all()
        article_id = self.request.query_params.get('article_id', None)
        category_id = self.request.query_params.get('category_id', None)
        if article_id is not None:
            queryset = queryset.filter(category__article_id=article_id)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["name", "article_id"]

class NewsList(ListView):
    """Список статей"""
    model = Article # модель, объекты которой предполагается выводить
    ordering = '-date' # # сортировка статей по дате публикации
    template_name = 'news.html' # шаблон с инструкциями о способах отображения пользователю всех объектов
    context_object_name = 'news' # список, в котором будут лежать все объекты
    paginate_by = 10

    def get_queryset(self):
        """Функция для получения списка новостей"""
        queryset = super().get_queryset() # получаем обычный запрос
        self.filterset = NewsFilter(self.request.GET, queryset) # сохраняем фильтрацию в объекте класса, чтобы потом добавить в контекст и использовать в шаблоне
        return self.filterset.qs # возвращаем из функции отфильтрованный список товаров
    def get_context_data(self, **kwargs):
        """Метод, позволяющий изменить набор данных, передаваемых в шаблон"""
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset # добавляем в контекст объект фильтрации
        # context['current_time'] = timezone.localtime(timezone.now()),
        context['timezones'] = pytz.common_timezones
        return context

    def post(self, request):
        """Добавление часового пояса в сессию через пост-запрос, обработанный middleware"""
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')



class NewsDetail(DetailView):
    """Информация о конкретной статье"""
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
    queryset = Article.objects.all()

    def get_object(self, *args, **kwargs):
        """Кэширование ДО обновления информации"""
        obj = cache.get(f'product-{self.kwargs["pk"]}', None)

        if not obj: # если объекта нет в кэше, то получаем его и записываем в кэш
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'product-{self.kwargs["pk"]}', obj) # кэш забирает значения по ключу, а если его нет, забирает None
        return obj

class NewsSearch(NewsList):
    template_name = 'news_search.html'
    context_object_name = 'news'

class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание новости"""
    raise_exception = True
    permission_required = ('news.add_article')
    model = Article
    form_class = NewsForm
    template_name = 'news_create.html'

class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование новости"""
    permission_required = ('news.change_article')
    raise_exception = True
    model = Article
    form_class = NewsForm
    template_name = 'news_edit.html' # news_create.html

class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Удаление новости"""
    permission_required = ('news.delete_article')
    raise_exception = True
    model = Article
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list') # шаблон, куда переотправим пользователя после успешного удаления

@login_required # только для зарегистрированных пользователей
@csrf_protect # автоматическая проверка csrf-токена в пользовательских формах
def subscriptions(request):
    """Подписки пользователя для рассылки писем"""
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscriber.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscriber.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscriber.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )


class CategoryListView(NewsList):
    model = Article
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk']) # id - поле, по которому хотим отфильтровать объект модели
        queryset = Article.objects.filter(category=self.category).order_by('-date') # -created_at
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required()
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категорий'
    return render(request, 'news/subscribe.html', {'category': category, 'message': message})

