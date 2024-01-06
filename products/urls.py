from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products_list, name="products"),
    path("", views.home, name="home"),
    path("add/<uuid:item_id>", views.add_to_cart, name="add_to_cart"),
]
