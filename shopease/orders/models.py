from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
    ])

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"