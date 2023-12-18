# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),
    path('families/', views.family_list, name='family_list'),
    path('admin/', admin.site.urls),
    path('family/<int:pk>/', views.family_detail, name='family_detail'),
    path('family/new/', views.family_new, name='family_new'),
    path('family/<int:pk>/edit/', views.family_edit, name='family_edit'),
    path('family/<int:pk>/delete/', views.family_delete, name='family_delete'),

    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
]
