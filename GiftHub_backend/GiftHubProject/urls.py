from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

# Swagger Setting
schema_view = get_schema_view(
    openapi.Info(
        title="GiftHub API",
        default_version='V1.0.0',
        description="GiftHub Django Swagger",
        terms_of_service="https://github.com/boostcampaitech6/level2-3-recsys-finalproject-recsys-04",
        contact=openapi.Contact(email="ksstpgns1@gmail.com"),
        license=openapi.License(name="GiftHub License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(('GiftHubApp.urls', 'api'))),  # GiftHub/urls.py 를 사용
]

if settings.DEBUG:  # Debug 환경일 때만 동작
    urlpatterns += [
        re_path(r'admin/', admin.site.urls),
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]