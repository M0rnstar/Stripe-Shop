from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'currency')
    list_filter = ('price',)
    search_fields = ('name',)
