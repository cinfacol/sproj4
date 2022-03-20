from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (Attribute, AttributeValue, Brand, Category, Media,
                     Product, Type)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ['attribute', 'attribute_value']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'id', 'slug', 'is_active']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'alt_text', 'image', 'created_at', 'updated_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'slug', 'media', 'brand', 'retail_price',
                    'store_price', 'discount_price', 'get_categories']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('name',)}
