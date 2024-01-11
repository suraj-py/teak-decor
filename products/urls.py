from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path("products/", views.products_list, name="products"),
    path("products/<str:category>", views.products_by_category, name="category"),
]
