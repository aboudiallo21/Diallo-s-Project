from django.urls import path
from . import views

urlpatterns = [
    path('', views.price_list, name='home'),
    path('families/', views.family_list, name='family_list'),
    path('family/<int:pk>/', views.family_detail, name='family_detail'),
    path('family/<int:pk>/edit/', views.family_edit, name='family_edit'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('family/new/', views.family_new, name='family_new'),
    path('family/<int:pk>/delete/', views.family_delete, name='family_delete'),
    path('prices/', views.price_list, name='price_list'),
    path('ponderations/', views.ponderation_list, name='ponderation_list'),
    path('ponderation/<int:pk>/', views.ponderation_detail, name='ponderation_detail'),
    path('ponderation/<int:pk>/edit/', views.ponderation_edit, name='ponderation_edit'),
    path('ponderation/add/', views.ponderation_add, name='ponderation_add'),
    path('ponderations/<int:pk>/delete/', views.ponderation_delete, name='ponderation_delete'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.product_new, name='product_new'),
    path('prices/add/', views.price_add, name='price_add'),
    path('prices/<int:pk>/', views.price_detail, name='price_detail'),
    path('prices/<int:pk>/edit/', views.price_edit, name='price_edit'),
    path('paniers/', views.panier_list, name='panier_list'),
    path('panier/<int:pk>/', views.panier_detail, name='panier_detail'),
    path('panier/<int:pk>/edit/', views.panier_edit, name='panier_edit'),
    path('panier/<int:pk>/delete/', views.panier_delete, name='panier_delete'),
    path('panier/new/', views.panier_add, name='panier_add'),
    path('pointvente/', views.pointvente_list, name='pointvente_list'),
    path('pointvente/add/', views.pointvente_add, name='pointvente_add'),

]
