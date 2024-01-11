from .models import CartItem

def cart_count(request):
    cart_items = CartItem.objects.all()
    cart_count = cart_items.count()
    return {'cart_count':cart_count}
