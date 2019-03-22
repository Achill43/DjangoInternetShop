from django.shortcuts import render
from .models import *

# Create your views here.

def oneProduct(request, id):
    product=Product.objects.get(id=id)
    return render(request, 'Shop/productPage.html', locals())
'''
def Products(request):
    return "Products"
    '''