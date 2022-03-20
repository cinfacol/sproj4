from django.contrib import admin

from .models import Post, ProductFavorite

# from cart.models import Order, OrderItem


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author', 'publish', 'status']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProductFavorite)
class ProductFavoriteAdmin(admin.ModelAdmin):
    list_display = ['product', 'client', 'status']


""" @admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ref_code', 'ordered']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'quantity', 'user', 'item'] """
