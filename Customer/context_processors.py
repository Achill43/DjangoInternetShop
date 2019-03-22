from .models import *

def getCustomer(request):
    user='false';
    if 'customer' in request.session:
        email = request.session['customer']
        customer=Customer.objects.get(email=email)
        user=customer.email

    return locals()