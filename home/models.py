from django.db import models
from django.contrib.auth.models import User , auth 

# Create your models here.


class basic_image(models.Model) :
    name = name = models.CharField(max_length=255 , null = True)
    image=models.ImageField(upload_to='images/basic/', blank=True, null=True)
    def __str__(self):
        return self.name

class category_model(models.Model) :
    category = models.CharField(max_length=255)
    def __str__(self) :
        return self.category

class product_model(models.Model) :
    category = models.ForeignKey(category_model, on_delete=models.CASCADE, null = True)
    top_product = models.BooleanField(default=False)
    name = models.CharField(max_length=255 , null = True)
    price = models.IntegerField(null = True)
    image = models.ImageField(upload_to='images/portfolio/', blank=True, null=True)
    description = models.CharField(max_length=255 , null = True)

    def __str__(self):
        return self.name 


class cart_model(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,default="N/A")
    product = models.ForeignKey(product_model,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(null = True)

class user_cart_model(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,default="N/A")
    product = models.ForeignKey(product_model,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(null = True)