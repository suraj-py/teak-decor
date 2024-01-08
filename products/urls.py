from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products_list, name="products"),
    path("cart/", views.cart_list, name="cart"),
    path("add/<uuid:item_id>", views.add_to_cart, name="add_to_cart"),
]
