from rest_framework import serializers
from .models import Supplier, Product, ProductDocument, Category


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "slug", "title", "desc", "image", "subtitle"]


class ProductDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDocument
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(
        source="supplier",
        queryset=Supplier.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    docs = ProductDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "subtitle",
            "slug",
            "image",
            "created_at",
            "in_stock",
            "price_text",
            "inci",
            "description",
            "function_text",
            "usage",
            "supplier",
            "supplier_id",
            "created_by",
            "docs",
        ]
        read_only_fields = ["id", "created_at", "created_by"]
