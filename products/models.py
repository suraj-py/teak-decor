import uuid
from django.db import models
from users.models import CustomUser


CATEGORY_CHOICES = (
    ('SO', 'Sofas'),
    ('BE','Beds'),
    ('CH','Chairs'),
    ('TB','Tables'),
    ('CU','Cupboards'),
)

class Item(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, blank=True)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item.title
