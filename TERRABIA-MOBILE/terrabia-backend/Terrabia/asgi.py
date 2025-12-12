"""
ASGI config for Terrabia project.
It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
import django

# Configure Django settings AVANT d'importer quoi que ce soit d'autre
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Terrabia.settings')
django.setup()  # ← TRÈS IMPORTANT !

# Maintenant tu peux importer les dépendances Django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Application HTTP Django
django_asgi_app = get_asgi_application()

# Import des routes WebSocket (APRÈS django.setup() pour éviter les imports circulaires)
try:
    from chat.routing import websocket_urlpatterns
    has_websockets = True
except ImportError:
    # Si pas de WebSockets, on continue sans
    websocket_urlpatterns = []
    has_websockets = False
except Exception as e:
    # En cas d'autre erreur (modèles non migrés, etc.)
    print(f"⚠️  Warning: Could not import chat.routing: {e}")
    websocket_urlpatterns = []
    has_websockets = False

# Configuration ASGI
if has_websockets and websocket_urlpatterns:
    application = ProtocolTypeRouter({
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        ),
    })
else:
    # Fallback si pas de WebSockets configurés
    application = ProtocolTypeRouter({
        "http": django_asgi_app,
    })