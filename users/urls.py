from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.UserView.as_view(), name='users'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_upd'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_del'),
]
