from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    list_filter = ('price',)
    search_fields = ('name', 'description')
    ordering = ('name',)
