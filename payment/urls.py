from django.urls import path

from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('<str:ref>/', views.verify_payment, name='verify_payment'),
]