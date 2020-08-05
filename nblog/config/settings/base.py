"""
Django settings for nblog project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(evj^kth%kz2@#dr9s1$vd6h(igx+c=ykb@oldafyb*ixt6t9-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PRODUCTION = False

if PRODUCTION:
    ALLOWED_HOSTS = ['www.nestorblog.com']
else:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


if PRODUCTION:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'compressor',
    'corsheaders',

    'rest_framework',
    'rest_framework.authtoken',

    'drf_yasg',
    'allauth',
    'allauth.account',
        # 'allauth.socialaccount',

    # 'dj_rest_auth',
    # 'dj_rest_auth.registration',


    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',

    'core',
    'accounts',
    'post',
    'profiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_URLS_REGEX = r'^/api/.*$'

CORS_ORIGIN_WHITELIST = [

    "http://localhost:3000",
]

DEFAULT_RENDERER_CLASSES = [
        'rest_framework.renderers.JSONRenderer',
    ]

if DEBUG:
    DEFAULT_RENDERER_CLASSES += [
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'accounts.views.permission.IsNotAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES
}

REST_AUTH_SERIALIZERS = {
    # "USER_DETAILS_SERIALIZER": 'accounts.serializers.CustomUserDetailsSerializer',
    # 'LOGIN_SERIALIZER': 'accounts.serializers.CustomUserLoginSerializer',
    # 'TOKEN_SERIALIZER': 'accounts.serializers.TokenSerializer',
    "PASSWORD_RESET_SERIALIZER": "accounts.serializers.PasswordResetSerializer",
    'REGISTER_SERIALIZER': "accounts.serializers.RegisterSerializer"
}

WSGI_APPLICATION = 'config.wsgi.app'

ACCOUNT_USERNAME_REQUIRED = False 
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'blogX',
        'USER': 'root',
        'PASSWORD': 'Amarillo90*',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/x-sass', 'django_libsass.SassCompiler'),
)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_mxTemplate"),
]

STATIC_ROOT = os.path.join(os.path.dirname(
    BASE_DIR), "static_cdn", "static_root")


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(
    BASE_DIR), "static_cdn", "media_root")


PROTECTED_ROOT = os.path.join(os.path.dirname(
    BASE_DIR), "static_cdn", "protected_media")

AUTH_USER_MODEL = 'accounts.User'

# Emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'contacto@nestorblog.com'
EMAIL_HOST_PASSWORD = 'AzulR0j01990*'
DEFAULT_FROM_EMAIL = 'Nestor <contacto@nestorblog.com>'

SITE_ID = 1

LOGIN_REDIRECT_URL = "/"

LOGIN_ON_EMAIL_CONFIRMATION = True
AUTHENTICATED_LOGIN_REDIRECTS ="/"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION=True
USERS_REQUIRE_APPROVAL = False
USERS_REQUIRE_TERMS_ACCEPTANCE = False
USERS_REQUIRE_VERIFICATION = True
ACCOUNT_CONFIRM_EMAIL_CLIENT_URL = "verify-email/?key={key}"
ACCOUNT_CONFIRM_PASSWORD_CLIENT_URL =  "confirm-pwd/?key={key}&uid={uid}"
USERS_ALLOW_REGISTRATION = True
# allauth
ACCOUNT_ADAPTER = 'config.adapters.AccountAdapter'
REST_SESSION_LOGIN = True

MAX_POST_LENGTH = 240
POST_ACTION_OPTIONS = ["like", "unlike", "repost"]

# APPEND_SLASH=False

FRONT_URL = '127.0.0.1:8000'

PROJECT_NAME = 'TeamSolutions'
# PROJECT_NAME = getattr(settings, "PROJECT_NAME", "TeamSolutions")
