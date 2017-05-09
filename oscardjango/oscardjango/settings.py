
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '8h9a&8g*q3-lym8*!t3ov99q-d0blm85k^5#+tp*m&0g)+$&a#'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'oscardjango.urls'

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

WSGI_APPLICATION = 'oscardjango.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'oscardjango',
        'USER': 'oscardjangouser',
        'PASSWORD': 'oscardjango',
        'HOST': 'localhost',
        'PORT': '5432',
    }
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

THEMES_DIR = os.path.join(BASE_DIR, "themes")
THEME = "oscartheme"
THEME_DIR = os.path.join(THEMES_DIR, THEME)
TEMPLATES_DIR = os.path.join(THEME_DIR, 'templates')
STATICFILES_DIRS = [os.path.join(THEME_DIR, "static")]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn')
MEDIA_URL = '/media/'
OSCAR_MISSING_IMAGE_URL = MEDIA_URL + 'image_not_found.jpg'

# this includes all the oscar default settins
from oscar.defaults import *

from oscar import OSCAR_MAIN_TEMPLATE_DIR

TEMPLATES[0]['DIRS'] = [
    TEMPLATES_DIR,
    OSCAR_MAIN_TEMPLATE_DIR
]

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
    
]

TEMPLATES[0]['OPTIONS']['libraries'] = {
    'sorl_thumbnail': 'sorl.thumbnail.templatetags.thumbnail',
}

from oscar import get_core_apps

INSTALLED_APPS = INSTALLED_APPS + [
    'django.contrib.gis',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django_extensions',
    'rest_framework',
    'widget_tweaks',
] + get_core_apps()

SITE_ID = 1

MIDDLEWARE += [
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
OSCAR_FROM_EMAIL = "prabhatiitbhu@gmail.com"
OSCAR_SEND_REGISTRATION_EMAIL = 'True'

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'
APPEND_SLASH = True

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

HAYSTACK_CONNECTIONS = {
     'default': {
         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
     },
 }


INTERNAL_IPS = ['127.0.0.1', '::1','localhost']


DATABASES['default']['ATOMIC_REQUESTS'] = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_DEFAULT_CURRENCY = "INR"
OSCAR_SHOP_TAGLINE = 'django oscar ecommerce marketplace'
OSCAR_SHOP_NAME = 'oscardjango'

