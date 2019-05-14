from django.conf import settings
from django.conf.urls import include, url
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.contrib import admin
from views import views, database_check_view

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="ThunderCAT APIs")

router = routers.DefaultRouter()
router.register(r"api/database_check", database_check_view.DatabaseViewSet)

urlpatterns = [
    url(r"^$", schema_view),
    url(r"^admin/", admin.site.urls),
    url(r"^api/auth/", include("djoser.urls")),
    url(r"^api/auth/", include("djoser.urls.jwt")),
    path(r"api/backend-status", views.index, name="index"),
    path("", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Browsable API login
urlpatterns += [
    url(r"^api/auth/", include("rest_framework.urls", namespace="rest_framework"))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r"^__debug__/", include(debug_toolbar.urls))]
