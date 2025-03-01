from django.db import models

class Item(models.Model):
    CURRENCY_CHOISES = (
        ('USD', 'Доллар'),
        ('RUB', 'Рубль')
    )

    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(default="", verbose_name="Описание товара")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Цена товара")
    currency = models.CharField(
        max_length=10, 
        choices=CURRENCY_CHOISES,
        default="USD", 
        verbose_name="Валюта"
        )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']
