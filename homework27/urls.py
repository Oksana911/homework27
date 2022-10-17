from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ads import views
from homework27 import settings
from rest_framework import routers
from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.MainView.as_view()),
    path('category/', include('ads.urls.categories_urls')),
    path('ad/', include('ads.urls.ads_urls')),
    path('selection/', include('ads.urls.selections_urls')),
    path('user/', include('users.urls')),
]
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
