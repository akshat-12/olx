from typing_extensions import Required
from django.db import models
from django.db.models.base import Model

class Owner(models.Model):
    name = models.CharField(blank = False, max_length=120,null=False)
    email = models.EmailField(blank = False, null=False)
    rollNo = models.CharField(blank = False, null=False)
    phoneNo = models.CharField(max_length=13)
    rating = models.FloatField(blank = True)
    profilePicture = models.ImageField(blank = True, null = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120, blank = False, null=False)
    price = models.IntegerField(blank = False, null=False)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank = False, null=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="products")
    dateCreated = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default = False)
    def __str__(self):
        return self.name

    @property
    def get_images(self):
        images = self.image_set.all()
        return images


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(blank=True, null=True, upload_to=f'images')
    def __str__(self):
        return self.product.name + " Image"
    
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url