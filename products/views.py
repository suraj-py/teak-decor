from django.shortcuts import render, redirect
from .models import Item, Cart, CartItem

def home(request):
    return render(request, 'base.html')

def products_list(request):
    products = Item.objects.all()
    context = {"products": products}
    return render(request, "products.html", context)

# def products_by_category(request, category):
#     products = Item.objects.filter(category=category)
#     context = {"products":products, "category":category}
#     return render(request, "products.html", context)

def cart_list(request):
    cart_items = CartItem.objects.all()
    cart_count = cart_items.count()
    context = {"cart_items":cart_items, "cart_count":cart_count}
    return render(request, "cart.html", context=context)

def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    cart_item.save()
    return redirect('products')

def increase_quantity(request, cart_id):
    cart_item = CartItem.objects.get(pk=cart_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def decrease_quantity(request, cart_id):
    cart_item = CartItem.objects.get(pk=cart_id)
    cart_item.quantity -= 1
    cart_item.save()
    if cart_item.quantity == 0:
        remove_cart_item(request, cart_id)
    return redirect('cart')

def remove_cart_item(request, cart_id):
    cart_item = CartItem.objects.get(pk=cart_id)
    cart_item.delete()
    return redirect('cart')
