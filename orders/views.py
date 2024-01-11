from django.shortcuts import render, redirect, reverse
from .models import Cart, CartItem
from products.models import Item

from django.views.generic import View
import stripe
from django.conf import settings

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

# add to cart view
def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    cart_item.save()
    return redirect('products')

# increase quantity by one
def increase_quantity(request, cart_id):
    cart_item = CartItem.objects.get(pk=cart_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

# decrease quantity by one
def decrease_quantity(request, cart_id):
    cart_item = CartItem.objects.get(pk=cart_id)
    cart_item.quantity -= 1
    cart_item.save()
    if cart_item.quantity == 0:
        remove_cart_item(request, cart_id)
    return redirect('cart')

# remove single item from cart
def remove_cart_item(request, cart_id):
    cart_item = CartItem.objects.get(pk=cart_id)
    cart_item.delete()
    return redirect('cart')


# ------------------Checkout Views-------------------------------

# Checkout view
class CreateCheckoutSessionView(View):
    def post(self, *args, **kwargs):
        host = self.request.get_host()

        cart_items = CartItem.objects.all()
        total = sum(item.item.price * item.quantity for item in cart_items)

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data':{
                        'currency':'usd',
                        'unit_amount': int(total) * 100,
                        'product_data':{
                            'name':'Tshirt',
                        }
                    },
                    'quantity': 1,
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
    return render(request, 'confirmation.html', context)

# view for handling failed payement
def paymentCancel(request):
    context = {
        'payment_status':'failed',
    }
    return render(request, 'confirmation.html', context)
