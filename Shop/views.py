from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import SubscriberForm
from Products.models import *
from Customer.models import *

def index(request):
    sales=Product.objects.filter(sale=True)[:6]
    hits=Product.objects.filter(hits=True)[:5]
    news=Product.objects.filter(news=True)    
    return render(request, 'Shop/homePage.html', locals())

def contactUs(request):
    form=SubscriberForm(request.POST or None)
    if request.method=='POST':
        form=form.save()

    return render(request, 'Shop/form.html', locals())

def eyestoppers(request, type, pageNumber):
    if type=='hits' :
        products=Product.objects.filter(hits=True)
    elif type=='news' :
        products=Product.objects.filter(news=True)
    elif type=='sale' :
        products=Product.objects.filter(sale=True)
    else :
        mark=ProductMark.objects.get(name=type)
        products=Product.objects.filter(mark=mark)

    pages=Paginator(products, 6)
    currentPage=pages.page(pageNumber)
    return render(request, 'Shop/hitsPage.html', locals())
