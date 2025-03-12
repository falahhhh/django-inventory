from django.db import models
from users.models import User
from products.models import Product

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('in', 'Incoming Stock'),
        ('out', 'Outgoing Stock'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type.upper()} - {self.date.strftime('%Y-%m-%d %H:%M')}"

class TransactionDetail(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="details")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="transaction_details")
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.transaction} - {self.product.name} ({self.quantity})"
