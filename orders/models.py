from django.db import models 
from home.models import Profile 
from product.models import Item

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
        ('cancelled','Cancelled')

    ]
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    menu = models.ForeignKey(Item, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits = 10 , decimal_places= 2)
    status = models.CharField(max_length = 10 , choices = STATUS_CHOICES, default = 'pending' )
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"
