from rest_framework import viewsets
from .models import Supplier, Product, ProductDocument,  Category
from .serializers import (
    SupplierSerializer,
    ProductSerializer,
    ProductDocumentSerializer,
    CategorySerializer,
)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related("supplier", "created_by").prefetch_related("docs")
    serializer_class = ProductSerializer
    lookup_field = "slug"

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(created_by=user)


class ProductDocumentViewSet(viewsets.ModelViewSet):
    queryset = ProductDocument.objects.all().select_related("product")
    serializer_class = ProductDocumentSerializer

