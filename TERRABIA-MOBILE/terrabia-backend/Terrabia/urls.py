from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Configuration Swagger/OpenAPI
schema_view = get_schema_view(
    openapi.Info(
        title="Terrabia API",
        default_version='v1',
        description="API Documentation for Terrabia E-commerce Platform",
        terms_of_service="https://terrabia.com/terms/",
        contact=openapi.Contact(email="contact@terrabia.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Administration Django
    path('admin/', admin.site.urls),
    
    # Authentification JWT (Simple JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API des utilisateurs (SANS DOUBLON)
    path('api/auth/', include('users.urls')),  # ← UNE SEULE FOIS
    
    # API des commandes
    path('api/orders/', include('orders.urls')),
    
    # API des produits
    path('api/products/', include('products.urls')),
    
    # API du chat (si activé)
    path('api/chat/', include('chat.urls')),
    
    # Documentation API (Swagger/ReDoc) - CORRIGÉ
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    # Route racine - Redirige vers la documentation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='home'),
]

# Pour servir les fichiers média en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)