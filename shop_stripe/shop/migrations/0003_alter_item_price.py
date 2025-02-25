# Generated by Django 5.1.6 on 2025-02-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_alter_item_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=9, verbose_name="Цена товара"
            ),
        ),
    ]
