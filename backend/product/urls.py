from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SupplierViewSet,
    ProductViewSet,
    ProductDocumentViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register(r"suppliers", SupplierViewSet, basename="supplier")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"documents", ProductDocumentViewSet, basename="productdocument")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
