from django.contrib import admin
from .models import *

# Register your models here.
class ProductForOrder(admin.TabularInline):
    model=ProductInOrder
    extra=0 #Додаткові поля при виведені масиву ImageForProduct

class OrderAdminDisplay(admin.ModelAdmin):
    list_display=["customerName", "customerEmail", "allSume"] #поля которые отображаются при выводе записей
    search_fields=["customerName"] #поля по корорым будет осуществлятся поиск
    inlines=[ProductForOrder]
    class Meta:
        model=Order

admin.site.register(Order, OrderAdminDisplay)
admin.site.register(Status)
admin.site.register(ProductInOrder)
admin.site.register(ProductInCart)