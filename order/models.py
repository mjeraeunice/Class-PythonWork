from django.db import models
from shipment.models import Shipping
from cart.models import Cart
from customer.models import Customer
# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, unique=True)
    customer_name = models.CharField(max_length=32)
    customer_email = models.EmailField(max_length=255)
    customer_phone_number = models.CharField(max_length=15)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=16, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ])
    shipment=models.OneToOneField(Shipping,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,null=True,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,null=True,on_delete=Customer)







