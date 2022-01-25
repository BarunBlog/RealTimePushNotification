from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import channels.layers
from django.dispatch import receiver
from asgiref.sync import async_to_sync
import json


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    
    def __str__(self):
        return self.name


status_choises = [
    ("Order Received", "Order Received"),
    ("Baking", "Baking"),
    ("Baked", "Baked"),
    ("Out for delivery", "Out for delivery"),
    ("Order Delivered", "Order Delivered")
]

class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=100)
    status = models.CharField(max_length=100, choices=status_choises, default="Order Received")
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
