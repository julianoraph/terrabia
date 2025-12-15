"""
Django settings for Terrabia project.
"""

import os
import sys
import logging.config
from pathlib import Path
from datetime import timedelta

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Ajouter le répertoire racine au PYTHONPATH pour éviter les erreurs d'import
if BASE_DIR not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# SECURITY
SECRET_KEY = 'django-insecure-%+qa135p%daj+(8ora1u4)!#g91#lez0j@h8#n1e*otcd2=cra'
DEBUG = True
ALLOWED_HOSTS = ['*']  # à restreindre en prod

# Application definition
INSTALLED_APPS = [
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
    'daphne',  # Daphne après Channels

    # Local apps
    'users',
    'products',
    'orders',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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
        'DIRS': [BASE_DIR / 'templates'],
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
        "BACKEND": "channels.layers.InMemoryChannelLayer"
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

# DRF + JWT
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

# Désactive la configuration automatique de Django
LOGGING_CONFIG = None

# Configuration unique des logs
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
        'chat': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Applique manuellement la configuration des logs
logging.config.dictConfig(LOGGING)

# ============================================================================
# DÉTECTION ET CONFIGURATION RAILWAY (PRODUCTION)
# ============================================================================

# Détection de l'environnement Railway
RAILWAY_ENV = os.environ.get('RAILWAY_ENVIRONMENT')

if RAILWAY_ENV:
    print("🚀 Configuration Railway détectée - Mode PRODUCTION")
    
    # Sécurité
    DEBUG = False
    
    # Utiliser la SECRET_KEY de Railway si disponible
    RAILWAY_SECRET_KEY = os.environ.get('SECRET_KEY')
    if RAILWAY_SECRET_KEY:
        SECRET_KEY = RAILWAY_SECRET_KEY
    else:
        print("⚠️ ATTENTION: SECRET_KEY Railway non trouvée, utilisation de la clé de dev")
    
    # Hosts autorisés
    ALLOWED_HOSTS = [
        '.up.railway.app',
        '.railway.app',
        'localhost',
        '127.0.0.1',
        # Ajoutez ici votre domaine personnalisé si vous en avez un
    ]
    
    # ==================== DATABASE POSTGRESQL ====================
    # Vérifier d'abord si DATABASE_URL existe
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if DATABASE_URL:
        try:
            # Essayer d'importer dj_database_url
            import importlib.util
            
            # Vérifier si dj_database_url est installé
            dj_database_url_spec = importlib.util.find_spec("dj_database_url")
            if dj_database_url_spec is not None:
                import dj_database_url
                DATABASES = {
                    'default': dj_database_url.config(
                        default=DATABASE_URL,
                        conn_max_age=600,
                        ssl_require=True
                    )
                }
                print("✅ Configuration PostgreSQL via DATABASE_URL")
            else:
                print("⚠️ dj_database_url non installé, tentative de configuration manuelle")
                raise ImportError("dj_database_url non installé")
        except Exception as e:
            print(f"⚠️ Erreur avec dj_database_url: {e}")
            # Fallback: configuration manuelle depuis les variables Railway
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': os.environ.get('PGDATABASE', 'railway'),
                    'USER': os.environ.get('PGUSER', 'postgres'),
                    'PASSWORD': os.environ.get('PGPASSWORD', ''),
                    'HOST': os.environ.get('PGHOST', 'localhost'),
                    'PORT': os.environ.get('PGPORT', '5432'),
                    'CONN_MAX_AGE': 600,
                    'OPTIONS': {
                        'sslmode': 'require',
                    }
                }
            }
            print("✅ Configuration PostgreSQL via variables Railway (fallback)")
    else:
        print("⚠️ DATABASE_URL non trouvé, vérifiez vos variables d'environnement Railway")
    
    # ==================== REDIS POUR CHANNELS ====================
    REDIS_URL = os.environ.get('REDIS_URL')
    if REDIS_URL:
        try:
            # Vérifier si channels_redis est installé
            channels_redis_spec = importlib.util.find_spec("channels_redis")
            if channels_redis_spec is not None:
                CHANNEL_LAYERS = {
                    "default": {
                        "BACKEND": "channels_redis.core.RedisChannelLayer",
                        "CONFIG": {
                            "hosts": [REDIS_URL],
                        },
                    }
                }
                print("✅ Redis configuré pour Channels")
            else:
                print("⚠️ channels_redis non installé")
                CHANNEL_LAYERS = {}
        except Exception as e:
            print(f"⚠️ Erreur avec channels_redis: {e}")
            CHANNEL_LAYERS = {}
    else:
        print("⚠️ REDIS_URL non trouvé, Channels désactivé en production")
        CHANNEL_LAYERS = {}
    
    # ==================== CORS POUR FRONTEND ====================
    CORS_ALLOW_ALL_ORIGINS = False
    
    # Récupérer les origines depuis les variables d'environnement ou utiliser les valeurs par défaut
    cors_origins = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')
    if cors_origins and cors_origins[0]:
        CORS_ALLOWED_ORIGINS = [origin.strip() for origin in cors_origins if origin.strip()]
    else:
        CORS_ALLOWED_ORIGINS = [
            "https://terrabia-jb7p.vercel.app",
            "https://terrabia.vercel.app",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ]
    
    print(f"✅ CORS autorisés: {CORS_ALLOWED_ORIGINS}")
    
    # Autoriser les credentials
    CORS_ALLOW_CREDENTIALS = True
    
    # ==================== SECURITY HTTPS ====================
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    print("✅ Configuration de sécurité HTTPS activée")
else:
    print("💻 Mode DÉVELOPPEMENT local")
    # Les valeurs par défaut définies en haut restent actives