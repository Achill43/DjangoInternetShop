from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

def register(request):
    user={'login': False, 'status': False}
    data=request.POST
    email=data.get('email')
    password=data.get('password')
    name=data.get('name')
    birthday=data.get('birthday')
    exists=Customer.objects.filter(email=email).exists()
    if exists:
        user['status']='exist'
    else:
        customer=Customer()
        customer.email=email
        customer.password=password
        customer.name=name
        customer.dateOfBirthday=birthday
        customer.save()
        request.session['customer'] = email
        user['email']=email
        user['status']='success'

    return JsonResponse(user)

def login(request):
    user={'login': False, 'status': False}
    data=request.POST
    email=data.get('email')
    password=data.get('password')
    exists=Customer.objects.filter(email=email).exists()
    if exists:
        customer=Customer.objects.get(email=email)
        if password==customer.password:
            user['email']=email
            request.session['customer'] = email
            user['status']='success'
        else :
            user['status']='password'
    else:
        user['status']='email'

    return JsonResponse(user)