from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gpk04t6mzzd0s3*&(ppr&qovstwd(1sc4--o3jvpgoe6f4r+)b'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST' : 'localhost',
        'USER': 'root',
        'PASSWORD': 'admin@1122'
    }
}