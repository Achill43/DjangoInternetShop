from django.shortcuts import render
from django.http import JsonResponse
from Products.models import Product
from .cart import Cart

# Create your views here.

def addToCart(request):
    data=request.POST
    id=data.get("productId")
    newCart={'totalQuantity': 0, 'totalPrice': 0}
    newCart['products']={}
    if 'shoppingCart' in request.session:
        newCart = request.session['shoppingCart']

    product=Product.objects.get(id=id)
    storeItem={}
    storeItem['quantity']=1
    storeItem['price']=product.price
    storeItem['name']=product.name
    if newCart['products'].get(id)!=None :
        newCart['products'][id]['quantity']=newCart['products'][id]['quantity']+1
        newCart['products'][id]['price']=product.price*newCart['products'][id]['quantity']
    else :
        newCart['products'][id]=storeItem
    
    
    newCart['totalQuantity']=newCart['totalQuantity']+1
    newCart['totalPrice']=newCart['totalPrice']+product.price

    request.session['shoppingCart'] = newCart
    return JsonResponse(newCart)

def getShoppingCart(request):
    shoppingCart={'totalQuantity': 0, 'totalPrice': 0}
    shoppingCart['products']={}
    if 'shoppingCart' in request.session:
        shoppingCart = request.session['shoppingCart']

    return shoppingCart

def deleteProductFromShoppingCart(request):
    data=request.POST
    id=data.get("productId")
    shoppingCart={'totalQuantity': 0, 'totalPrice': 0}
    shoppingCart['products']={}
    if 'shoppingCart' in request.session:
        oldCart = request.session['shoppingCart']
        shoppingCart=oldCart

    shoppingCart['totalQuantity']=shoppingCart['totalQuantity']-shoppingCart['products'][id]['quantity']
    shoppingCart['totalPrice']=shoppingCart['totalPrice']-shoppingCart['products'][id]['price']
    del shoppingCart['products'][id]
    request.session['shoppingCart'] = shoppingCart
    return JsonResponse(shoppingCart)

