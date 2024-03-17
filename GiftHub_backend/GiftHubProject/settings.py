"""
Django settings for GiftHubProject project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-57i2bu1u3-rf*3#q4^x#4q4=#$m-_-dbj674(egsahl7pgso6('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['101.79.11.75', '127.0.0.1', '0.0.0.0', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'GiftHubApp',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [  # API 리턴에 사용되는 기본 렌더 클래스 지정
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',  # 인증된 사용자만 API 액세스
    # ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework.authentication.SessionAuthentication',  # Session 인증 클래스
    #     'rest_framework.authentication.TokenAuthentication',  # Token 인증 클래스
    # ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # API 결과가 페이지로 나뉘어 표시되는 방식 제어
    # 'PAGE_SIZE': 10  # 페이지 크기
    
    # 'DEFAULT_FILTER_BACKENDS': [  # API 클라이언트가 사용할 수 있는 필터링 옵션을 정의
    #     'rest_framework.filters.SearchFilter',
    #     'rest_framework.filters.OrderingFilter',
    # ],
    
    # 'DEFAULT_THROTTLE_CLASSES': [  # 클라이언트가 API에 요청을 할 수 있는 속도를 제한
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle',
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/day',
    #     'user': '1000/day',
    # }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GiftHubProject.urls'

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

WSGI_APPLICATION = 'GiftHubProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

## Router
DATABASE_ROUTERS = [
    'GiftHubApp.routers.AuthRouter',
    'GiftHubApp.routers.GiftHubRouter',
]

DATABASES = {
    'default': {  # Django 관리 DB
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'django',
    'USER': 'recsys4',
    'PASSWORD': 'recsys1234',
    'HOST': '223.130.160.153',
    'PORT': '2306'
    },
    
    'gifthub': {  # gift DB
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'gifthub_test',
    'USER': 'recsys4',
    'PASSWORD': 'recsys1234',
    'HOST': '223.130.160.153',
    'PORT': '2306'
    }
}

# Representative Category Image
IMAGE_URL = '/image/'
IMAGE_ROOT = os.path.join(BASE_DIR, 'GiftHubApp/images')

# mlflow url
MODEL_DOWNLOAD_YN = "N"
MLFLOW_URL = "http://101.79.11.75:8010"
PATH_CATEGORY_PROBA = os.path.join(BASE_DIR, 'mlartifacts/category_proba')

# model bert4rec
PATH_BERT4REC = os.path.join(BASE_DIR, 'mlartifacts/bert4rec')


LGBM_PROBA = "http://101.79.11.75:8011/invocations"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
}