from django.db import models
from .order import Order
from .payment_type import PaymentType

class Revenue(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tip = models.FloatField()
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
