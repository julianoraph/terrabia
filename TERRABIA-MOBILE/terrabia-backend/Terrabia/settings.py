"""
Django settings for Terrabia project.
"""

import os
import logging.config
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

# Channels (Redis ou InMemory) - CONFIG PAR DÉFAUT POUR LE DEV
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"   # marche sans Redis
    }
}

# Database → SQLite (parfait en dev) - CORRIGÉ : Cohérent avec requirements.txt
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # ← RESTE SQLite pour la simplicité en dev
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
STATICFILES_DIRS = [BASE_DIR / 'static']  # ← DÉFINITION UNIQUE ICI
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
# CONFIGURATION DES LOGS (UNIFIÉE POUR TOUS LES ENVIRONNEMENTS)
# ============================================================================

# Désactive la configuration automatique de Django pour éviter l'erreur configure_logging
LOGGING_CONFIG = None

# Configuration unique des logs (appliquée dans tous les environnements)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'users': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'products': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'orders': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Applique manuellement la configuration des logs
logging.config.dictConfig(LOGGING)

# ============================================================================
# CONFIGURATION RAILWAY (PRODUCTION)
# ============================================================================

# Détection de l'environnement Railway
RAILWAY_ENV = os.environ.get('RAILWAY_ENVIRONMENT') or os.environ.get('DATABASE_URL')

if RAILWAY_ENV:
    # ==================== PRODUCTION SUR RAILWAY ====================
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
    
    # ==================== DATABASE POSTGRESQL (CORRIGÉ) ====================
    # Essayer d'utiliser dj_database_url, sinon utiliser les variables directes
    database_config = {}
    
    if os.environ.get('DATABASE_URL'):
        try:
            import dj_database_url
            database_config = dj_database_url.config(
                default=os.environ.get('DATABASE_URL'),
                conn_max_age=600,
                ssl_require=True
            )
        except ImportError:
            # Fallback: construire la config manuellement depuis les variables Railway
            database_config = {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.environ.get('PGDATABASE', 'railway'),
                'USER': os.environ.get('PGUSER', 'postgres'),
                'PASSWORD': os.environ.get('PGPASSWORD', ''),
                'HOST': os.environ.get('PGHOST', 'localhost'),
                'PORT': os.environ.get('PGPORT', '5432'),
            }
    else:
        # Si DATABASE_URL n'existe pas, utiliser les variables PostgreSQL standard
        database_config = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('PGDATABASE', 'railway'),
            'USER': os.environ.get('PGUSER', 'postgres'),
            'PASSWORD': os.environ.get('PGPASSWORD', ''),
            'HOST': os.environ.get('PGHOST', 'localhost'),
            'PORT': os.environ.get('PGPORT', '5432'),
        }
    
    DATABASES = {
        'default': database_config
    }
    
    # ... reste de ta configuration Railway ...

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
    else:
        # Si pas de Redis sur Railway, on désactive Channels pour la production
        CHANNEL_LAYERS = {}
    
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
    
    # ==================== SECURITY HTTPS ====================
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Note: La configuration LOGGING reste celle définie plus haut
    # Pas besoin de la redéfinir ici

# Pas de bloc 'else:' pour le développement local car
# les valeurs par défaut définies en haut du fichier sont déjà parfaites pour le dev.