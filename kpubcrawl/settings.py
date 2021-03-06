"""
Django settings for kpubcrawl project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd#2knmw77x)%e+1a@y3b+in$ck69f=906cl-nvjfdv^0vws#7t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seoulcrawl',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'kpubcrawl.urls'

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

WSGI_APPLICATION = 'kpubcrawl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATES_CONTENT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backedns',
    'social.apps.django_app.context_processors.login_redirect',
)
AUTHENTICATION_BACKENDS = (
    "social.backends.facebook.FacebookOAuth2",
    "social.backends.google.GoogleOAuth2",
    "social.backends.twitter.TwitterOAuth",
    "django.contrib.auth.backends.ModelBackend",        
)

#로그인 후 되돌아올 URL
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

#인증 URL의 NAMESPACE
SOCIAL_AUTH_LOGIN_NAMESPACE = 'social'

#Facebook
SOCIAL_AUTH_FACEBOOK_KEY = "278725945810246"
SOCIAL_AUTH_FACEBOOK_SECRET = '32ebc4c72ed5141fd29ef1e0e71a3a4f'

#Google
#Social_AUTH_GOOGLE_OAUTH2_KEY = ''
#Social_AUTH_GOOGLE_OAUTH2_SECRET = ''

#Twitter
#SOCIAL_AUTH_TWITTER_KEY = ''
#SOCIAL_AUTH_TWITTER_SECRET = ''

#세션 객체를 직렬화 하는 처리기
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

#미디어 처리
STATIC_URL = '/static/'
STATICFILES_DIRS = (("img","C:/Users/jinwook/kpubcrawling/seoulcrawl/static_files/img/"),)
STSTIC_ROOT = os.path.join(BASE_DIR,'collected_statics')
MEDIA_URL = '/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static_files')
