from django.db import models
from users.models import CustomUser
from products.models import Item

# Cart Model
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

    def __str__(self):
        return self.user.username

# Cart Items
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item.title

    @property
    def item_total(self):
        return self.quantity * self.item.price
