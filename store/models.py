from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand_names",null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_names",null=True)
    product_name = models.CharField(max_length=50)
    product_code = models.IntegerField(null=True)
    package_type = models.CharField(max_length=50,null=True)
    net_weight = models.CharField(max_length=50,null=True)
    unit_per_box = models.CharField(max_length=50,null=True)
    gross_weight = models.CharField(max_length=50,null=True)
    dimensions = models.CharField(max_length=50,null=True)
    barcode_number = models.IntegerField(null=True)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = "/static/Titiz_067.jpg"
        return url
