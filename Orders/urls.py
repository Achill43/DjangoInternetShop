from django.urls import path
from . import views

urlpatterns=[
    path('addToCart', views.addToCart, name='addToCart'),
    path('deleteFromCart', views.deleteProductFromShoppingCart, name='deleteFromCart')
]