from django.shortcuts import render
from .models import Item, Category

# Home Page View
def home(request):
    products = Item.objects.all()[4:8]
    context = {'products':products}
    return render(request, 'home.html', context)

# View for listing all products
def products_list(request):
    products = Item.objects.all()
    category_names = Category.objects.all()
    context = {"products": products, "category_names":category_names}
    return render(request, "products.html", context)

# View for listing products by category
def products_by_category(request, category):
    products = Item.objects.filter(category=category)
    context = {"products":products, "category":category}
    return render(request, "products.html", context)

def detail_page(request, product_id):
    product = Item.objects.filter(pk=product_id)
    context = {'product':product}
    return render(request, 'detail_page.html', context)

