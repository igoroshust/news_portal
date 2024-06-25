"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y^-6z!!anwgeea1m75$lss6vmk*2an58m8t)0nlat@irw3je5i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] # список достоверных хостов
# SECURE_PROXY_SSL_HEADER # проверка безопасного подключения, даже если данные поступают из http
# SECURE_SSL_REDIRECT # используется для перенаправления всех запросов с http на https
# SESSION_COOKIE_SECURE / CSRF_COOKIE_SECURE # флаги, устанавливающие передачу данных cookie только по https

SITE_URL = 'http://127.0.0.1:8000'


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', # управление сессиями
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ----------------
    # Новые приложения
    # ----------------
    'app',
    'news',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'fpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
    'board',
    'rest_framework',
]

SITE_ID = 1

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.middlewares.TimezoneMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', # статистические страницы
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Russian'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/news'

ACCOUNT_EMAIL_REQUIRED = True # поле email является обязательным
ACCOUNT_UNIQUE_EMAIL = True # поле email является уникальным
ACCOUNT_USERNAME_REQUIRED = False # поле username является необязательным
ACCOUNT_AUTHENTICATION_METHOD = 'email' # аутентификация через email
ACCOUNT_EMAIL_VERIFICATION = 'none' # верификация почты отсутствует

ACCOUNT_FORMS = {
    "signup": "accounts.forms.CustomSignupForm",
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # класс отправителя сообщений
EMAIL_PORT = 465 # порт для приёма писем почтовым сервером
EMAIL_HOST = 'smtp.yandex.ru' # хост почтового сервера
EMAIL_HOST_USER = 'NewsPortal.project' # логин пользователя почтового сервиса
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD') # пароль пользователя почтового сервиса
EMAIL_USE_TLS = False # необходимость использования TLS
EMAIL_USE_SSL = True # необходимость использования SSL

DEFAULT_FROM_EMAIL = 'NewsPortal.project@yandex.ru' # почтовый адрес отправителя по умолчанию

EMAIL_SUBJECT_PREFIX = '' # текст в начале письма с сообщением
SERVER_EMAIL = 'NewsPortal.project@yandex.ru' # адрес почты, от имени которой будет отправляться письмо при вызове mail_admins и mail_manager.
MANAGERS = (
    ('Igor', 'igoroshust@yandex.ru'),
)

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25 # количество секунд выполнения команды

# ------ Celery ------
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

# ------ Кэширование ------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

# ---- Пагинация ----
# REST_FRAMEWORK = {
#    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
#    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#    'PAGE_SIZE': 10,
#    'DEFAULT_PERMISSION_CLASSES': [
#            'rest_framework.permissions.IsAuthenticated',
#        ]
# }