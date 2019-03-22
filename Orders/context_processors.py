from Orders.views import getShoppingCart

def gettingShoppingCart(request):
    shoppingCart=getShoppingCart(request)
    productsInCart=shoppingCart['products']

    return locals()
