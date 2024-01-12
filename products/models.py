import uuid
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Items Model
class Item(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.title

