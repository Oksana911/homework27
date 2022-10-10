from django.urls import path
from ads import views


urlpatterns = [

    path('', views.CategoryView.as_view(), name='cat'),
    path('<int:pk>/', views.CategoryDetailView.as_view(), name='cat_detail'),
    path('create/', views.CategoryCreateView.as_view(), name='cat_create'),
    path('<int:pk>/upd/', views.CategoryUpdateView.as_view(), name='cat_upd'),
    path('<int:pk>/del/', views.CategoryDeleteView.as_view(), name='cat_del'),
]