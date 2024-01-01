from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
