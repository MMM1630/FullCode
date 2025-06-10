from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from fullcode.views import *
from config import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="FullCode.kg",
        default_version='v1',
        description="Документация FullCode.kg API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('api/fullcode', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/project-contact/', ProjectContactView.as_view(), name='project-contact'),
    path('api/services/', ServicesView.as_view(), name='services'),
    path('api/project/', ProjectView.as_view(), name='project'),
    path('api/comands/', ComandsView.as_view(), name='comands'),
    path('api/school-contact/', SchoolContactView.as_view(), name='school-contact'),
    path('api/courses/', CoursesView.as_view(), name='courses'),
    path('api/pros/', ProsView.as_view(), name='pros'),
    path('api/certificates/', CertificatesView.as_view(), name='certificates'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)