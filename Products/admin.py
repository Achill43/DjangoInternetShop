from django.contrib import admin
from .models import *

# Register your models here.
class ImageInlineProducts(admin.TabularInline):
    model=ImageForProduct
    extra=0 #Додаткові поля при виведені масиву ImageForProduct 

class ProductDisplay(admin.ModelAdmin):
    list_display=['id', 'name', 'publish', 'price']
    search_field=['name']
    inlines=[ImageInlineProducts]
    class Meta:
        model=Product

admin.site.register(Product,  ProductDisplay)
admin.site.register(ImageForProduct)
admin.site.register(ProductMark)