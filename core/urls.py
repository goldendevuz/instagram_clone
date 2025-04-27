from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from core.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT
from apps.v1.shared.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('user/', include('apps.v1.users.urls')),
    path('post/', include('apps.v1.post.urls')),
    path('api-auth/', include('rest_framework.urls')),  # Important for login/logout
    path('test-login/', test, name='test'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)