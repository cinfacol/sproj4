from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Product, Media, Type, Brand, Attribute, AttributeValue


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
    list_display = ['name', 'slug', 'is_active']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['alt_text', 'image', 'created_at', 'updated_at']


class MediaInline(admin.TabularInline):
    model = Media


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        MediaInline,
    ]
    list_display = ['name', 'slug', 'brand', 'retail_price',
                    'store_price', 'discount_price', 'created_at']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('name',)}
