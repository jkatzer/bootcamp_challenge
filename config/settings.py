"""
Django settings for bootcamp project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to grunt file if necessary in callback to find gruntfile. Currently working without.
GRUNT_PATH = os.path.join(BASE_DIR, 'gruntfile.js') 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4^ud9sklmezjdixej=rh(cv*@cx_417utduvmel^j3!*_sv++b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


######################################################################
## Application definition
######################################################################

INSTALLED_APPS = (
    # django components
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # external apps
    'rest_framework',
    'django_extensions',
    # my apps 
    'forum_backend',
    # toolset, including grunt tasks
    'tools',
)

# Middleware is happening in the middle of every process: things like session management, authentication, etc. ALways available to call (with import)
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

# rool URL configuration. from here we tell the app about the admin, other services, and redirect everything else to the forum urlconf.
ROOT_URLCONF = 'config.urls'


# templates, don't have that much to say here. 
# If you want to change the way templating works (folder-wise), simply add to the DIRS directory, and turn off the APP_DIRS boolean.
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


########################################################################
## WSGI 
## https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
########################################################################
WSGI_APPLICATION = 'config.wsgi.application'


##################################################################
## Database Config 
## https://docs.djangoproject.com/en/1.8/ref/settings/#databases
##################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


###################################################################
## Time, Internationalization Settings
## (Defaults, I didnt mess with this at all)
## https://docs.djangoproject.com/en/1.8/topics/i18n/
###################################################################
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

####################################################################
## Static File (CSS, JavaScript, Images) and Uploaded Media Settings (S3 or Local)
## https://docs.djangoproject.com/en/1.8/howto/static-files/
####################################################################

# give static assets a /static/item url
STATIC_URL = '/static/'

# add node_modules and frontend directories to Django's directories to query for files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend'),
    os.path.join(BASE_DIR, 'node_modules'),
)

## Rest Framework settings
REST_FRAMEWORK = {
    'PAGE_SIZE': 10
}