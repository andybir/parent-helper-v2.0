from .base import *

DEBUG = False

ADMINS = (
    ('admin', 'abirosak@gmail.com')
)

ALLOWED_HOSTS = ['parenthelperproject.com', 'www.parenthelperproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'parent_helper',
        'USER': 'parent_helper',
        'PASSWORD': '**********',
    }
}