from django.shortcuts import render
from .models import Item

def products_list(request):
    products = Item.objects.all()
    context = {"products": products}
    return render(request, "products.html", context)
