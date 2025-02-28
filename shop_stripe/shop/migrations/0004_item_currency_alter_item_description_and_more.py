# Generated by Django 5.1.6 on 2025-02-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_alter_item_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="currency",
            field=models.CharField(default="USD", max_length=10, verbose_name="Валюта"),
        ),
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(null=True, verbose_name="Описание товара"),
        ),
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Цена товара"
            ),
        ),
    ]
