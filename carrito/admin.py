from django.contrib import admin
from .models import ShoppingCart, Order, OrderDetail

# Register your models here.

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['curso', 'price', 'user','created_at']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['price', 'user', 'code','created_at']


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'curso', 'price','created_at']