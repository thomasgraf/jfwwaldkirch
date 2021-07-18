from .base import *
import os

env = os.environ.copy()

SECRET_KEY=env['SECRET_KEY']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env['DBNAME'],
        'USER': env['DBUSER'],
        'PASSWORD': env['DBPASSWORD'],
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


try:
    from .local import *
except ImportError:
    pass
