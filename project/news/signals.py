# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from .models import Article
#
# @receiver(post_save, sender=Article) # receiver добавляется, чтобы функция стала сигналом (декоратор получает событие, которое запускает процесс)
# def news_created(instance, created, **kwargs):
#     """Создание статьи"""
#     if not created:
#         return
#
#     emails = User.objects.filter(
#         subscriptions__category=instance.category
#     ).values_list('email', flat=True)
#
#     subject = f'Новая статья в категории {instance.category}' # заголовок письма
#
#     text_content = (
#         f'Статья: {instance.name} <br>'
#         f'Дата публикации {instance.date} <br><br>'
#         f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#
#     html_content = (
#         f'Название: {instance.name} <br>'
#         f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
#         f'Читать статью по ссылке</a>'
#     )
#
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()

# =======
# from django.core.mail import EmailMultiAlternatives
# from django.dispatch import receiver
# from django.db.models.signals import m2m_changed
# from django.template.loader import render_to_string
#
# from news.models import ArticleCategory
#
# from project import settings
#
#
# def send_notifications(preview, title, subscribers):
#     """Функция отправки сообщений"""
#     html_content = render_to_string(
#         'article_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     # формируем сообщение
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email='NewsPortal.project@yandex.ru',
#         to=subscribers,
#     )
#     msg.attach_alternative(html_content, 'text/html') # добавляем к сообщению шаблон
#     msg.send() # отправляем сообщение
# @receiver(m2m_changed, sender=ArticleCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     """Уведомление о новом посте"""
#     if kwargs['action'] == 'article_add': # add_aricle
#         categories = instance.category.all() # categoryName
#         subscribers_emails = []
#
#         for cat in categories:
#             subscribers = cat.subscribers.all() # список подписчиков
#             subscribers_emails += [s.email for s in subscribers] # список почт подписчиков
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)
