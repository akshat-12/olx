from django.db import models
from django.db.models.base import Model

class Owner(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phoneNo = models.CharField(max_length=13)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="products")
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(blank=True, null=True, upload_to=f'images')
    def __str__(self):
        return self.product.name + " Image"