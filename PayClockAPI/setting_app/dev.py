import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-only-insecure-key-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Security: Never use '*' in ALLOWED_HOSTS, even in development
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',  # For Docker development
]

# CORS settings for development
CORS_ALLOW_ALL_ORIGINS = False  # Never use True in production
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",    # React dev server
    "http://127.0.0.1:3000",
    "http://localhost:8080",    # Vue.js dev server
    "http://127.0.0.1:8080",
    "http://localhost:5173",    # Vite dev server
]

# Additional CORS settings for development
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For collectstatic

# Media files
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Development-specific settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django Debug Toolbar (optional but helpful)
try:
    import debug_toolbar
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
    INTERNAL_IPS = ['127.0.0.1']
except ImportError:
    pass

# Less strict password validation in development
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4,  # Lower for easier development
        }
    },
]

# Logging for development
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}