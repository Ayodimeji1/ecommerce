from .base import *
import dj_database_url


DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:$$ayodimeji22@localhost:5432/ecommerce", conn_max_age=600
    )
}

SECRET_KEY = 'django-insecure--jvr+ki2x=jaeem!$qdi7ovsumqxzixl)m)yy3ci2qgo93$9wi'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'


