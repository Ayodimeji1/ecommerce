from django.urls import path
from product import views

urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.category, name='category')
]
