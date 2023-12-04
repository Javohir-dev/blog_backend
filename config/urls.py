from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Blog Project",
        default_version="v1",
        description="This project contains APIs for Get All informations.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="javohir.py@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("info.urls")),
    path("api/v1/", include("edu.urls")),
    path("api/v1/", include("blog.urls")),
    # Schema Swagger Ui
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
