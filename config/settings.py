# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
Django settings for chnl_expl_project.

Environmental variables triggered in project's env27_chnl_expl/bin/activate, when using runserver,
  or env27_chnl_expl/bin/activate_this.py, when using apache via passenger.
"""

import json, logging, os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['CHNNLS__SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = json.loads( os.environ['CHNNLS__DEBUG_JSON'] )  # will be True or False
# TEMPLATE_DEBUG = DEBUG

ADMINS = json.loads( os.environ['CHNNLS__ADMINS_JSON'] )
MANAGERS = ADMINS

ALLOWED_HOSTS = json.loads( os.environ['CHNNLS__ALLOWED_HOSTS'] )  # list


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'email_app',
    'primes_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.passenger_wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = json.loads( os.environ['CHNNLS__DATABASES_JSON'] )


# Django Channels
# http://channels.readthedocs.org/en/latest/index.html

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            # "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
            "hosts": [ 'redis://localhost:6379' ],
        },
        "ROUTING": "config.routing.channel_routing",
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = os.environ['CHNNLS__STATIC_URL']
STATIC_ROOT = os.environ['CHNNLS__STATIC_ROOT']  # needed for collectstatic command


# Templates

# TEMPLATE_DIRS = json.loads( os.environ['CHNNLS__TEMPLATE_DIRS'] )  # list
TEMPLATES = json.loads( os.environ['CHNNLS__TEMPLATES_JSON'] )  # list of dict(s)


# Email
EMAIL_HOST = os.environ['CHNNLS__EMAIL_HOST']
EMAIL_PORT = int( os.environ['CHNNLS__EMAIL_PORT'] )


# sessions

# <https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-SESSION_SAVE_EVERY_REQUEST>
# Thinking: not that many concurrent users, and no pages where session info isn't required, so overhead is reasonable.
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# logging

## disable module loggers
# existing_logger_names = logging.getLogger().manager.loggerDict.keys()
# print '- EXISTING_LOGGER_NAMES, `%s`' % existing_logger_names
logging.getLogger('requests').setLevel( logging.WARNING )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level':'DEBUG',
            'class':'logging.FileHandler',  # note: configure server to use system's log-rotate to avoid permissions issues
            'filename': os.environ.get(u'CHNNLS__LOG_PATH'),
            'formatter': 'standard',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'email_app': {
            'handlers': ['logfile'],
            'level': os.environ.get(u'CHNNLS__LOG_LEVEL'),
        },
        'primes_app': {
            'handlers': ['logfile'],
            'level': os.environ.get(u'CHNNLS__LOG_LEVEL'),
        },
    }
}

