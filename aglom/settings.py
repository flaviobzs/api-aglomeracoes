import os
from decouple import config
from os.path import exists
from pathlib import Path
import environ

env = environ.Env()
BASE_DIR = environ.Path(__file__) - 2


if exists(BASE_DIR.path('.env')):
    env.read_env(f'{BASE_DIR.path(".env")}')


SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

#SECRET_KEY = config('SECRET_KEY')
#DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app_auth',
    'app_denuncias',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

'''
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ['http://localhost:*']
CORS_ORIGIN_REGEX_WHITELIST = ['http://localhost:*']
'''

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

ROOT_URLCONF = 'aglom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'aglom.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

from dj_database_url import parse as dburl
#default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')


DATABASES = {
    'default': env.db()
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        #rest_framework.permissions.IsAuthenticated',
        #rest_framework.permissions.IsAuthenticatedOrReadOnly',  #libera somente o READ da api'''
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
