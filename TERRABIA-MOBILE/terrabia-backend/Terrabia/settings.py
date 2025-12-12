"""
Django settings for Terrabia project.
"""

import os
from pathlib import Path
from datetime import timedelta
from decouple import config  # même si tu n'utilises pas .env pour l'instant

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-%+qa135p%daj+(8ora1u4)!#g91#lez0j@h8#n1e*otcd2=cra'
DEBUG = True
ALLOWED_HOSTS = ['*']  # à restreindre en prod

# Application definition
INSTALLED_APPS = [
    'daphne',  # ← DOIT ÊTRE EN PREMIER pour ASGI/Channels
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'django_filters',
    'corsheaders',
    'channels',

    # Local apps
    'users',
    'products',
    'orders',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← AJOUTÉ pour static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',          # ← CORS avant CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Terrabia.urls'

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

WSGI_APPLICATION = 'Terrabia.wsgi.application'
ASGI_APPLICATION = 'Terrabia.asgi.application'

# Channels (Redis ou InMemory)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"   # marche sans Redis
    }
}

# Database → SQLite (parfait en dev)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Custom User Model
AUTH_USER_MODEL = 'users.User'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Dakar'
USE_I18N = True
USE_TZ = True

# Static & Media
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Whitenoise pour servir les fichiers statiques
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF + JWT (LA PARTIE CRUCIALE)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Simple JWT → configuration propre
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

# CORS → tout autorisé en dev
CORS_ALLOW_ALL_ORIGINS = True

# Swagger settings
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

# ============================================================================
# CONFIGURATION RAILWAY (PRODUCTION)
# ============================================================================

# Détection de l'environnement Railway
RAILWAY_ENV = os.environ.get('RAILWAY_ENVIRONMENT') or os.environ.get('DATABASE_URL')

if RAILWAY_ENV:
    # ==================== PRODUCTION SUR RAILWAY ====================
    
    # Sécurité
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
    
    # Hosts autorisés
    ALLOWED_HOSTS = [
        '.up.railway.app',
        '.railway.app',
        'localhost',
        '127.0.0.1',
    ]
    
    # ==================== DATABASE POSTGRESQL ====================
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=True
        )
    }
    
    # ==================== REDIS POUR CHANNELS ====================
    REDIS_URL = os.environ.get('REDIS_URL')
    if REDIS_URL:
        CHANNEL_LAYERS = {
            "default": {
                "BACKEND": "channels_redis.core.RedisChannelLayer",
                "CONFIG": {
                    "hosts": [REDIS_URL],
                },
            }
        }
    
    # ==================== CORS POUR FRONTEND VERCEL ====================
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = [
        "https://terrabia-jb7p.vercel.app",
        "https://terrabia.vercel.app",
        "http://localhost:3000",  # Dev local
        "http://127.0.0.1:3000",  # Dev local
    ]
    
    # Autoriser les credentials (cookies, auth headers)
    CORS_ALLOW_CREDENTIALS = True
    
    # ==================== STATIC FILES ====================
    # Whitenoise est déjà configuré plus haut
    
    # ==================== SECURITY HTTPS ====================
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # ==================== LOGGING ====================
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
            'level': 'INFO',
        },
    }
    
    # ==================== MEDIA FILES (UPLOADS) ====================
    # Sur Railway, utilise un service externe comme Cloudinary ou AWS S3
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    # AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    # AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
    
else:
    # ==================== DÉVELOPPEMENT LOCAL ====================
    
    # Pour éviter les warnings static en dev
    STATICFILES_DIRS = [BASE_DIR / "static"]
    
    # CORS dev
    CORS_ALLOW_ALL_ORIGINS = True
    
    # Channels dev (InMemory)
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer"
        }
    }