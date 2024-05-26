from celery import shared_task
import time
import datetime
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils import timezone

from news.models import Article, Category

@shared_task
@receiver(post_save, sender=Article) # receiver добавляется, чтобы функция стала сигналом (декоратор получает событие, которое запускает процесс)
def news_created(instance, created, **kwargs):
    """Создание статьи"""
    if not created:
        return

    emails = User.objects.filter(subscriptions__category=instance.category).values_list('email', flat=True)

    subject = f'Новая статья в категории {instance.category}' # заголовок письма

    text_content = (
        f'Статья: {instance.name} <br>'
        f'Дата публикации {instance.date} <br><br>'
        f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )

    html_content = (
        f'Название: {instance.name} <br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Читать статью по ссылке</a>'
    )

    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

@shared_task
def weekly_newsletter():
    """Еженедельная рассылка статей по подписке"""
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7) # время начала отсчёта = сегодня - 7 дней назад
    articles = Article.objects.filter(date__gte=last_week)
    categories = set(articles.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': 'http://127.0.0.1:8000',
            'articles': articles,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email='NewsPortal.project@yandex.ru',
        to=subscribers, # список почт подписчиков
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

# @shared_task
# def hello():
#     time.sleep(10)
#     print('Hello!')