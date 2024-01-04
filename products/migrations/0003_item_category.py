# Generated by Django 4.2.8 on 2024-01-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_item_id_alter_item_image_alter_item_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("SO", "Sofas"),
                    ("BE", "Beds"),
                    ("CH", "Chairs"),
                    ("TB", "Tables"),
                    ("CU", "Cupboards"),
                ],
                max_length=2,
            ),
        ),
    ]