from django.urls import path
from . import views


urlpatterns = [

    path("cart/", views.cart_list, name="cart"),
    path("add/<uuid:item_id>", views.add_to_cart, name="add_to_cart"),
    path("increase/<int:cart_id>", views.increase_quantity, name="increase_quantity"),
    path("decrease/<int:cart_id>", views.decrease_quantity, name="decrease_quantity"),
    path("remove/<int:cart_id>", views.remove_cart_item, name="remove_cart_item"),

    path("create-checkout-session/", views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path("payment-success", views.paymentSuccess, name='payment-success'),
    path("payment-cancel", views.paymentCancel, name='payment-cancel'),
]
