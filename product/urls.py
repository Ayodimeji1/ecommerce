from django.urls import path
from product import views

urlpatterns = [
    path('search', views.search, name="search"),
    path('shop/', views.shop, name='shop'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    # path('<slug:category_slug>/<slug:product_slug>/', views.blank, name='blank'),
    path('<slug:category_slug>/', views.category, name='category')
]
