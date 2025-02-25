from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(blank=True, null=True, verbose_name="Описание товара")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена товара")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']
