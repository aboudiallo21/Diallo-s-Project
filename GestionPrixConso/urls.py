"""
URL configuration for GestionPrixConso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path



from django.urls import path
from gestion_produits import views


# urls.py

from django.urls import path
#from . import views

urlpatterns =[
    path('', views.product_list, name='home'),
    path('admin/', admin.site.urls),
    path('families/', views.family_list, name='family_list'),
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

#urlpatterns = [
 #   path('', views.liste_familles_produit, name='accueil'),  # Redirection vers la liste des familles


 #   path('admin/', admin.site.urls),
#path('', include('gestion_produits.urls')),
#]
