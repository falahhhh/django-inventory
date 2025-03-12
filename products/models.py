from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="product")
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.code} - {self.name}"
