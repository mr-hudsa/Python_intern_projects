from django.db import models

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class ProductItem(models.Model):
    category = models.ForeignKey(ProductCategory, related_name="products", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} ({self.category.category_name})"
