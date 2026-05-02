from django.contrib import admin
from .models import *
from .models import Product, ProductVariant, ProductImage, Order, OrderItem, Profile, Wishlist

# Variant inside Product
class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


# Multiple images inside Product
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'base_price', 'stock', 'is_active']
    prepopulated_fields = {"slug": ("name",)}

    inlines = [ProductVariantInline, ProductImageInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price', 'status', 'created_at']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'variant', 'price', 'quantity']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']