from .base import *
import os
# setup postgres database

DEBUG = False
ALLOWED_HOSTS = ['10.0.0.239', '0.0.0.0', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['http://10.0.0.239']
STATIC_ROOT = '/app/static/'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'stocktrackapp',
#         'USER': 'postgres',
#         'PASSWORD': '',
#         'HOST': '0.0.0.0',
#         'PORT': '',
#     }
# 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}