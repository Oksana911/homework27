from django.urls import path
from ads import views

urlpatterns = [
    path('', views.SelectionListView.as_view(), name='sel_list'),
    path('<int:pk>/', views.SelectionDetailView.as_view(), name='sel_detail'),
    path('create/', views.SelectionCreateView.as_view(), name='sel_post'),
    path('<int:pk>/update/', views.SelectionUpdateView.as_view(), name='sel_upd'),
    path('<int:pk>/delete/', views.SelectionDeleteView.as_view(), name='sel_del'),
]
