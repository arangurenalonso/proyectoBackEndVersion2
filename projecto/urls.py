"""projecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view (
    openapi.Info (
        title='APP Gastos',
        default_version='v1',
        description='Aplicación Pachaqtec',
        contact=openapi.Contact(email='aranguren.alonso@gmail.com')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('pachaqtec/', include('app.urls')),
    path('carrito/', include('carrito.urls')),
    path('auth/', include('authentication.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-w-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='shecma-redoc')
]
