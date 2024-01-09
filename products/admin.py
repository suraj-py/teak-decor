from django.contrib import admin
from .models import Item, Cart, CartItem, Category

admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
