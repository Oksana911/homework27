from django.urls import path
from ads import views

urlpatterns = [
    path('', views.AdView.as_view(), name='ad'),
    path('<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('create/', views.AdCreateView.as_view(), name='ad_post'),
    path('<int:pk>/upload_image/', views.AdImageUpdateView.as_view(), name='ad_upl_img'),
    path('<int:pk>/update/', views.AdUpdateView.as_view(), name='ad_upd'),
    path('<int:pk>/delete/', views.AdDeleteView.as_view(), name='ad_del'),
]
