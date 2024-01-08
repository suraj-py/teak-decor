from django.shortcuts import render, redirect
from .models import Item, Cart, CartItem

def home(request):
    return render(request, 'base.html')

def products_list(request):
    products = Item.objects.all()
    context = {"products": products}
    return render(request, "products.html", context)

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
