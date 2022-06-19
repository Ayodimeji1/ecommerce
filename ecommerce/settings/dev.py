from .base import *
import dj_database_url


DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:$$ayodimeji22@localhost:5432/ecommerce", conn_max_age=600
    )
}

SECRET_KEY = 'django-insecure--jvr+ki2x=jaeem!$qdi7ovsumqxzixl)m)yy3ci2qgo93$9wi'

FLUTTERWAVE_PUBLIC_KEY = 'FLWPUBK-e013ff06845fd0620d94a098b47bd1cc-X'
FLUTTERWAVE_SECRET_KEY = 'FLWSECK-ef5816f1c26217ea095976395b9339cc-X'

# PAYSTACK_SECRET_KEY = 'sk_test_05e65d231a09f6b2d86495fa3e526d807287ccf8'
# PAYSTACK_PUBLIC_KEY = 'pk_test_abf9ebd652514f64bfb004be60e673c92224aa56'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'


