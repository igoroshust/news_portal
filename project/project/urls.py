"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from news.views import *
from rest_framework import routers

router = routers.DefaultRouter() # объект дефолтного роутера
router.register(r'article', ArticleViewset) # связь роутера с вьюсетом
router.register(r'category', CategoryViewset)



urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')), # news.urls
    path('accounts/', include('allauth.urls')),
    path('test/', include('board.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}),
         name='swagger-ui'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls))
    # path('accounts/', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('pages/', include('django.contrib.flatpages.urls')),
]
