"""
Django settings for revolt-backend project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

import dj_database_url
import raven
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('REVOLT_SECRET_KEY', default='replace_this_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('REVOLT_DEBUG', cast=bool, default=True)

ALLOWED_HOSTS = config(
    'REVOLT_ALLOWED_HOSTS',
    # Support "host1, host2" etc
    cast=lambda v: [s.strip() for s in v.split(',')],
    default='*')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'data_models',
    'graphene_django',
    'django_summernote',
    'colorfield',
    'sorl.thumbnail',
    'sorl_cropping',
    'raven.contrib.django.raven_compat',
    'solo',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    # Set this using the environment variable "DATABASE_URL"
    'default': dj_database_url.config(default="sqlite:///%s/db.sqlite3" % BASE_DIR),
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'nb'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = config("REVOLT_STATIC_ROOT", default=os.path.join(BASE_DIR, 'staticfiles'))

MEDIA_URL = '/media/'
MEDIA_ROOT = config("REVOLT_MEDIA_ROOT", default=os.path.join(BASE_DIR, 'mediafiles'))

SUMMERNOTE_CONFIG = {
    'toolbar': [['style', ['bold', 'italic', 'underline', 'clear']], ['list', ['ul', 'ol']],
                ['media', ['link', 'picture',
                           'videoAttributes']], ['tools', ['redo', 'undo', 'fullscreen']]],
    'js': ('/static/summernote-video-attributes.js', ),
    'css': ('/static/summernote-video-attributes.css', )
}

CKEDITOR_UPLOAD_PATH = 'ckeditor'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Article': [
            {
                'name': 'styles',
                'items': ['Styles', 'Format', 'FontSize', 'Source', '-', 'ShowBlocks', 'Maximize'],
            },
            '/',
            {
                'name': 'justify',
                'items': ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            },
            {
                'name':
                'basicstyles',
                'items': [
                    'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript',
                    'Blockquote', '-', 'RemoveFormat'
                ],
            },
            {
                'name': 'colors',
                'items': ['TextColor', 'BGColor'],
            },
            {
                'name': 'clipboard',
                'items': ['Cut', 'Copy', 'SelectAll', '-', 'Undo', 'Redo'],
            },
            '/',
            {
                'name': 'paragraph',
                'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            },
            {
                'name': 'links',
                'items': ['Link', 'Unlink', 'Anchor']
            },
            {
                'name':
                'insert',
                'items':
                ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'Iframe', 'Youtube']
            },
        ],
        'toolbar':
        'Article',
        'height':
        800,
        'width':
        1000,
        'forcePasteAsPlainText':
        True,
        'font_names':
        'Arial/Arial, Helvetica, sans-serif',
        'font_defaultLabel':
        'Arial',
        'youtube_responsive':
        True,
        'youtube_disabled_fields': [
            'txtWidth',
            'txtHeight',
            'txtEmbed',
        ],
        'tabSpaces':
        4,
        'extraPlugins':
        ','.join([
            # your extra plugins here
            'uploadimage',
            'autolink',
            'image2',
            'youtube',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}

THUMBNAIL_ENGINE = 'sorl_cropping.engine.CropEngine'

raven_dsn = config('REVOLT_RAVEN_DSN', default='')
if raven_dsn:
    RAVEN_CONFIG = {
        'dsn': raven_dsn,
        # Use git to determine release
        'release': raven.fetch_git_sha(BASE_DIR),
    }

GRAPHENE = {'SCHEMA': 'api_graphql.schema.schema'}
