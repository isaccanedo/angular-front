"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from rest_framework_simplejwt import views as jwt_views
from banco import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Configuração do Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Doc - BancoClick",
      default_version='v1',
      description="",
      terms_of_service="",
      contact=openapi.Contact(email="henriquevic012@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

#Configuração de rotas personalizadas
router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
    path(r'doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('token/',  jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('usuario/existe/<usuario>/', views.UsuarioExiste.as_view()),
    path('admin/', admin.site.urls),
]
