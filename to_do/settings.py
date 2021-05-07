"""
Django settings for to_do project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'todo_app.apps.TodoAppConfig',
    'rest_framework',
    'rest_framework.authtoken',
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

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'to_do.urls'

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

WSGI_APPLICATION = 'to_do.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'to_do_db',
#         'USER': 'naile',
#         'PASSWORD': '',
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
#     }
# }

if DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR  + '/' + 'db.sqlite3',
    }
}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'to_do_db',
            'USER': 'naile',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }
# 'rest_framework.permissions.IsAdminUser'

REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
   'DEFAULT_PERMISSION_CLASSES': ( 'rest_framework.permissions.IsAuthenticated', ),
   
}


from datetime import timedelta


...


#JWT stand for JSON Web Token and it is an authentication strategy used by client/server applications where the client is a Web application using JavaScript and some frontend framework like Angular, React or VueJS.The JWT is acquired by exchanging an username + password for an access token and an refresh token.
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  #which specifies how long access tokens are valid
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # how long refresh tokens are valid.
    'ROTATE_REFRESH_TOKENS': False,   #When set to True, if a refresh token is submitted to the TokenRefreshView, a new refresh token will be returned along with the new access token. 
    'BLACKLIST_AFTER_ROTATION': True,  #refresh tokens submitted to the TokenRefreshView to be added to the blacklist 
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',   #TWO types either HMAC  or RSA for HMAC 'HS256', 'HS384', 'HS512: SIGNING_KEY setting will be used as both the signing key and the verifying key.  asymmetric RSA RS256', 'RS384', 'RS512' SIGNING_KEY setting must be set to a string that contains an RSA private key. Likewise, the VERIFYING_KEY
    'SIGNING_KEY': SECRET_KEY,  #content of generated tokens.
    'VERIFYING_KEY': None,   #The verifying key which is used to verify the content of generated tokens
    'AUDIENCE': None,   #The audience claim to be included in generated tokens and/or validated in decoded tokens
    'ISSUER': None,  #ssuer claim to be included in generated tokens 

    'AUTH_HEADER_TYPES': ('Bearer',),   #Authorization: Bearer <token> ('Bearer', 'JWT')
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'username',  #The database field from the user model that will be included in generated tokens to identify users.
    'USER_ID_CLAIM': 'username',  #value of 'user_id' would mean generated tokens include a “user_id” claim that contains the user’s identifier.

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',), #token_type
    'TOKEN_TYPE_CLAIM': 'token_type',  #The claim name that is used to store a token’s type

    'JTI_CLAIM': 'jti',   #The claim name that is used to store a token’s unique identifier.

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
