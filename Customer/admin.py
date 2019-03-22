from django.contrib import admin
from .models import *

# Register your models here.

class CustomerPreviewAdmin(admin.ModelAdmin):
    list_display=["email", "name"] #поля которые отображаются при выводе записей
    search_fields=["email"] #поля по корорым будет осуществлятся поиск
    class Meta:
        model=Customer

admin.site.register(Customer, CustomerPreviewAdmin)