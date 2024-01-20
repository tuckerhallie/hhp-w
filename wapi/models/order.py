from django.db import models
from .user import User
from .order_type import OrderType

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    name = models.CharField(max_length=70)
    customer_phone = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE)
    is_closed = models.BooleanField(default=False)
