from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(null = True)
    price = models.DecimalField(max_digits = 15, decimal_places = 2)
    sold = models.BooleanField(default = False)
