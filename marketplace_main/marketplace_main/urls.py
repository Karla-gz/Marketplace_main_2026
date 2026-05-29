from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # <-- Revisa que tengas esta importación
from django.conf.urls.static import static  # <-- Y esta también

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

# Esto es lo que hace la magia para que se vean las fotos en tu compu:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)