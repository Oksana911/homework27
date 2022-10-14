from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ads import views
from homework27 import settings
from rest_framework import routers
from users.views import LocationViewSet


router = routers.SimpleRouter()
router.register('location', LocationViewSet)

# router_1 = routers.SimpleRouter()
# router_1.register('ad', AdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.MainView.as_view()),
    path('category/', include('ads.category_urls')),
    path('ad/', include('ads.ads_urls')),
    path('user/', include('users.urls')),
]
urlpatterns += router.urls
# urlpatterns += router_1.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
