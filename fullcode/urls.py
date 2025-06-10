from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from fullcode.views import *


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

]