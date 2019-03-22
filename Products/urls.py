from django.urls import path
from . import views

urlpatterns=[
    #path('products', views.Products, name='products'),
    path('<int:id>/', views.oneProduct, name='product'),
]