from django.contrib import admin
from .models.ProductsUpload import ProductsUpload
from .models.Products import Product
from .models.Category import Category
from .models.contactform import Contact
# Register your models here.

admin.site.register(ProductsUpload)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contact)