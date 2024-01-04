from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products_list, name="products_page"),
    path("", views.home, name="home"),
]
