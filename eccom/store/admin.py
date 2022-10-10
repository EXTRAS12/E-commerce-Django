from django.contrib import admin

from .models import Category, Product, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    """Добавление товара в админке"""
    list_display = ['title', 'category', 'price', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    """Добавление товара в админке"""
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
