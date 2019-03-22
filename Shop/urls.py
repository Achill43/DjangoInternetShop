from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('contactus', views.contactUs, name='contactus'),
    path('<str:type><int:pageNumber>', views.eyestoppers, name='eyestoppers'),
    path('<str:type><int:pageNumber>',  views.eyestoppers, name='eyestoppers'),
    path('<str:type><int:pageNumber>', views.eyestoppers, name='eyestoppers'),
    path('<str:name><int:pageNumber>', views.eyestoppers, name='eyestoppers'),
]