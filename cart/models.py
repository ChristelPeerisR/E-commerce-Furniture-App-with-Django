from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=50)
    desc =  models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    CHOICES = (
        ('Bed', 'Bed'),
        ('Sofa', 'Sofa'),
        ('Table', 'Table'),
        ('Living Room', 'Living Room'),
        ('Bed Room', 'Bed Room'),
        ('Dinning', 'Dinning')
    )

    category = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.title

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.title}'