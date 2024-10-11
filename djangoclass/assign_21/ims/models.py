from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    suppliers = models.ManyToManyField(Supplier, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
