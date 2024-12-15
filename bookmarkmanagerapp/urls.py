
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_bookmark, name='add_bookmark'),
    path('edit/<str:pk>/', views.edit_bookmark, name='edit_bookmark'),
    path('delete/<str:pk>/', views.delete_bookmark, name='delete_bookmark'),
    path('add-category/', views.add_category, name='add_category'), 
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]
