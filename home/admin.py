from django.contrib import admin

from .models import category_model,product_model , cart_model , basic_image 
# Register your models here.





admin.site.register(category_model)

admin.site.register(product_model)

admin.site.register(cart_model)

admin.site.register(basic_image)

