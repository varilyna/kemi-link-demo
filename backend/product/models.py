from django.db import models
from django.conf import settings


class Supplier(models.Model):
    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to="suppliers/", blank=True, null=True)

    site = models.URLField(blank=True)

    fit = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return self.name
    

class Category(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    title = models.CharField(max_length=255)

    desc = models.CharField(max_length=500, blank=True)

    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    subtitle = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)

    subtitle = models.CharField(max_length=255, blank=True)

    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    image = models.ImageField(upload_to="products/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    in_stock = models.BooleanField("In stock", default=True, db_index=True)

    price_text = models.CharField(max_length=100, blank=True)

    inci = models.CharField(max_length=255, blank=True)

    description = models.TextField(blank=True)

    function_text = models.TextField(blank=True)

    usage = models.TextField(blank=True)

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )

    def __str__(self) -> str:
        return self.title


class ProductDocument(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="docs",
    )

    name = models.CharField(max_length=255)

    url = models.URLField()

    def __str__(self) -> str:
        return f"{self.name} ({self.product})"
