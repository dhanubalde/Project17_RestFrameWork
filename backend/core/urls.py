
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api/search/', include('search.urls')),
    path('api/products/', include('products.urls')),
    path('api/v2/', include('core.routers'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
