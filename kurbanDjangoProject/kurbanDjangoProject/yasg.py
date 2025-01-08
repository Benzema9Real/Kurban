from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Создание схемы OpenAPI для документации
schema_view = get_schema_view(
    openapi.Info(
        title="Anime",
        default_version='v1',
        description="Описание вашего API",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Включение Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Включение ReDoc UI
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]