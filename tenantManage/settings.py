"""
Django settings for tenantManage project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'utz1(qmp84-&ir-3ials7&l5nii@y9nj-8zk#c3%rp176j4)2%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'engine',
    'grappelli',
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

ROOT_URLCONF = 'tenantManage.urls'

WSGI_APPLICATION = 'tenantManage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tenant',
        'USER': 'mysql',
        'PASSWORD': 'mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = os.path.join(PROJECT_DIR,'static').replace('\\','/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    ("images", os.path.join(STATIC_ROOT,'images').replace('\\','/')),
    ("css",    os.path.join(STATIC_ROOT,'css').replace('\\','/')),
    ("js",     os.path.join(STATIC_ROOT,'js').replace('\\','/')),
    ("custom-plugins",     os.path.join(STATIC_ROOT,'custom-plugins').replace('\\','/')),
    ("jui",     os.path.join(STATIC_ROOT,'jui').replace('\\','/')),
    ("plugins",     os.path.join(STATIC_ROOT,'plugins').replace('\\','/')),
    ("bootstrap",     os.path.join(STATIC_ROOT,'bootstrap').replace('\\','/')),
    ("swf",     os.path.join(STATIC_ROOT,'swf').replace('\\','/')),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)



#template
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(name)s %(asctime)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(name)s %(asctime)s %(pathname)s %(module)s %(lineno)d %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'django_request':{
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(lineno)d %(message)s status_code:%(status_code)d',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'django_db_backends':{
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(lineno)d %(message)s duration:%(duration).3f sql:%(sql)s params:%(params)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'custom_log_file':{
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, 'logs/django.log'),#you need define your VAR_ROOT variable that points to your project path,and mkdir a logs directory in your project root path.
            'backupCount': 5,
            'maxBytes': '16777216', # 16megabytes(16M)
            'formatter': 'verbose'
        },
        'django_request_logfile':{
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, 'logs/django_request_logfile.log'),#you need define your VAR_ROOT variable that points to your project path,and mkdir a logs directory in your project root path.
            'backupCount': 5,
            'maxBytes': '16777216', # 16megabytes(16M)
            'formatter': 'django_request'
        },
        'django_db_backends_logfile':{
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, 'logs/django_db_backends_logfile.log'),#you need define your VAR_ROOT variable that points to your project path,and mkdir a logs directory in your project root path.
            'backupCount': 5,
            'maxBytes': '16777216', # 16megabytes(16M)
            'formatter': 'django_db_backends'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins','django_request_logfile'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['django_db_backends_logfile',],
            'level': 'WARNING',
            'propagate': True,
        },
        'customapp': {#then you can change the level to control your custom app whether to output the debug infomation
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
