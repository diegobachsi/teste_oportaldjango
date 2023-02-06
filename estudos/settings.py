"""
Django settings for estudos project.

Generated by 'django-admin startproject' using Django 2.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from decouple import config

from django.db.backends.mysql.base import DatabaseWrapper

DatabaseWrapper.data_types['DateTimeField'] = 'datetime' # fix for MySQL 5.5


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/a

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$+r+anux9dvm#^mt0*i#k+d2-tzmf92xilj%1fyqgnji7@w7s_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    'topicos',
    'accounts',
    'videos',
    'cursos',
    'forum',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'estudos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
		'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

#social_app configurações personalizadas 
AUTHENTICATION_BACKENDS = [ 
    'social_core.backends.google.GoogleOAuth2', 
    'social_core.backends.facebook.FacebookOAuth2', 
    'django.contrib.auth.backends.ModelBackend', 
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

WSGI_APPLICATION = 'estudos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

'''DATABASE_URL = 'postgresql://postgres:uG5Y5Pj9g9DvsuwWL0Iy@containers-us-west-123.railway.app:7548/railway'

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_e7f5f1e97d6491c',
        'USER': 'b04b3899b228a0',
        'PASSWORD': '5150b335',
        'HOST': 'us-cdbr-east-02.cleardb.com', #or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
                'init_command': 'SET default_storage_engine=INNODB',
            },
        }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ADMINS = (
    ('admin-web', 'equipe.gdek@gmail.com')
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'equipe.gdek@gmail.com'
#EMAIL_HOST_PASSWORD = 'gmail2020django'
EMAIL_HOST_PASSWORD = 'tjdeebkhmanprbmz'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = 'equipe.gdek@gmail.com'

CONTACT_EMAIL = 'equipe.gdek@gmail.com'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/index/'

LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_FACEBOOK_KEY = '313237803996731'        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '8a4d9826e87fa390824ab2938de45ea9'  # App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '299815273927-4g8dspl106n9cn3kcph3ku6suajtdmti.apps.googleusercontent.com' 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
