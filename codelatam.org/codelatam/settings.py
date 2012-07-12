# Django settings for codelatam project.

""" Import os
Modificado: Alex Dzul 10/07/2012
Motivo: Para el dinamismo entre sistemas operativos
"""
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
# Esta linea de codigo se cambia cuando se trabaja localmente
IS_REMOTO = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Se realiza para ser multi plataforma y trabajar remotamente y localmente
if IS_REMOTO: # Si el proyecto es remoto entonces
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': 'codelatam_bd',                      # Or path to database file if using sqlite3.
			'USER': 'alexdzul',                      # Not used with sqlite3.
			'PASSWORD': 'alex2012',                  # Not used with sqlite3.
			'HOST': 'bd.codelatam.org',                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		}
	}
else: # De lo contrario si es local entonces se utiliza la siguiente configuracion
	DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
				'NAME': 'codelatam_bd',                      # Or path to database file if using sqlite3.
				'USER': 'root',                      # Not used with sqlite3.
				'PASSWORD': 'root',                  # Not used with sqlite3.
				'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
				'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
			}
		}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

""" MEDIA_ROOT Multiplataforma
Modificacion: Alex Dzul 10/07/2012
Motivo: Se cambia esta linea para que funcione dinamicamente en cualquier sistema operativo
"""

MEDIA_ROOT = os.path.join('../public/','media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6gf85%7s=kl%jgxtwqk$0=3&^h(-@6p$^^9n%$b3n$4(p6dqgh'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'codelatam.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__),'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'codelatam.apps.home',
)
