"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
BASE_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm!aji^@#s#bh9j8v0ct#fl1&9$a^pqq1d6f5ti49=unv3z3bn('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

from os.path import normpath  # noqa

ROOT_DIR = normpath(os.path.dirname(os.path.realpath(__file__)) + '/')


def rel(*paths):
    return os.path.join(ROOT_DIR, *paths)

# Application definition


INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'staticunderscorei18n',
    'django.contrib.auth',
    'django.contrib.contenttypes',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
    ('fr', 'French'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (rel('templates/'), )
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.realpath(os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'
STATIC_UNDERSCORE_I18N_ROOT = STATIC_ROOT
STATIC_UNDERSCORE_I18N_OUTPUT_DIR = 'jsunderscorei18n'
STATIC_UNDERSCORE_I18N_FILENAME_FUNCTION = 'staticunderscorei18n.utils.default_filename'
STATIC_UNDERSCORE_TEMPLATES = {
    'popup_variable': 'underscore/popup.html',
}
STATIC_UNDERSCORE_TEMPLATES_DOMAIN = 'underscore_templates'
