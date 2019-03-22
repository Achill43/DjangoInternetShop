from django.contrib import admin
from .models import *

# Register your models here.

class SubscribersAdminDisplay(admin.ModelAdmin):
    list_display=["name", "email", "phone"] #поля которые отображаются при выводе записей
    search_fields=["name"] #поля по корорым будет осуществлятся поиск

    class Meta:
        model=Subscribers

admin.site.register(Subscribers, SubscribersAdminDisplay)
