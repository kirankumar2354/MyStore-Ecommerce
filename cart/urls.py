
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_list, name='cart_list'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
