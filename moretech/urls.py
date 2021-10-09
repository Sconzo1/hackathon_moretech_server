from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Панель управление More.Tech 3.0"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('authentication.urls')),
    path('', include('spectacular.urls')),
]
