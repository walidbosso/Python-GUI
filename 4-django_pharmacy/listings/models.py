from django.db import models

# Create your models here.
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_in_stock = models.PositiveIntegerField()

