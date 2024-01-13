from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.conf import settings
from django.contrib import messages

from .models import Cart, CartItem
from products.models import Item

import stripe

# stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

# View list all products in the cart
def cart_list(request):
    cart_items = CartItem.objects.all()
    cart_count = cart_items.count()
    sub_total = sum(item.item.price * item.quantity for item in cart_items)
    if sub_total > 300:
        shipping = 'FREE'
    else:
        shipping = 20

    if shipping == 'FREE':
        total = sub_total
    else:
        total = sub_total + shipping
    context = {
            "cart_items":cart_items,
            "cart_count":cart_count,
            "sub_total":sub_total,
            "shipping" : shipping,
            "total": total,
            }
    return render(request, "cart.html", context=context)

# Check if the item is already in the cart
def item_already_in_cart(item_id):
    return CartItem.objects.filter(item_id=item_id).exists()

# add to cart view
@login_required()
def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if item_already_in_cart(item_id):
        messages.warning(request, 'Item is already in the cart.')
    else:
        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        cart_item.save()
        messages.success(request, "Item added in the cart.")
    return redirect('products')

# increase quantity by one
@login_required()
def increase_quantity(request, cart_id):
    cart_item = CartItem.objects.get(pk=cart_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

# decrease quantity by one
@login_required()
def decrease_quantity(request, cart_id):
    cart_item = CartItem.objects.get(pk=cart_id)
    cart_item.quantity -= 1
    cart_item.save()
    if cart_item.quantity == 0:
        remove_cart_item(request, cart_id)
    return redirect('cart')

# remove single item from cart
@login_required()
def remove_cart_item(request, cart_id):
    cart_item = CartItem.objects.get(pk=cart_id)
    cart_item.delete()
    messages.success(request, "Item removed from the cart.")
    return redirect('cart')

@login_required()
def clear_cart(request):
    cart_items = CartItem.objects.all()
    cart_items.delete()
    return redirect('cart')



# ------------------Checkout Views-------------------------------

# Checkout view
class CreateCheckoutSessionView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        host = self.request.get_host()

        cart_items = CartItem.objects.all()
        count = cart_items.count()
        total = sum(item.item.price * item.quantity for item in cart_items)

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data':{
                        'currency':'usd',
                        'unit_amount': int(total) * 100,
                        'product_data':{
                            'name': '#order45654',
                        }
                    },
                    'quantity': count,
                },
            ],
            mode='payment',
            success_url = "http://{}{}".format(host,reverse('payment-success')),
            cancel_url = "http://{}{}".format(host,reverse('payment-cancel')),
        )

        return redirect(checkout_session.url, code=303)

# view for handling successful payment
def paymentSuccess(request):
    context = {
        'payment_status':'success',
    }
    print('successful payment: clearing cart')
    clear_cart(request)
    return render(request, 'confirmation.html', context)

# view for handling failed payement
def paymentCancel(request):
    context = {
        'payment_status':'failed',
    }
    return render(request, 'confirmation.html', context)
