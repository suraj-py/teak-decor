# Generated by Django 4.2.8 on 2024-01-11 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_category_alter_item_category"),
    ]

    operations = [
        migrations.RemoveField(model_name="cartitem", name="cart",),
        migrations.RemoveField(model_name="cartitem", name="item",),
        migrations.DeleteModel(name="Cart",),
        migrations.DeleteModel(name="CartItem",),
    ]
