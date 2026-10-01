from django.contrib import admin
from .models import Supplier, Product, ProductDocument, Category


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "site", "fit")
    search_fields = ("name",)


class ProductDocumentInline(admin.TabularInline):
    model = ProductDocument
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "subtitle", "price_text", "supplier", "created_at")
    list_filter = ("supplier",)
    search_fields = ("title", "subtitle", "slug", "inci")
    inlines = [ProductDocumentInline]


@admin.register(ProductDocument)
class ProductDocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product", "url")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "subtitle")
    search_fields = ("title", "slug", "subtitle")