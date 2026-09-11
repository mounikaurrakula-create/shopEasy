from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('products/', views.products, name='products'),

    path(
        'products/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'cart/add/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'cart/increase/<int:product_id>/',
        views.increase_cart,
        name='increase_cart'
    ),

    path(
        'cart/decrease/<int:product_id>/',
        views.decrease_cart,
        name='decrease_cart'
    ),

    path(
        'cart/remove/<int:product_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),
]