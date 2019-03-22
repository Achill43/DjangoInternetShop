from .models import ProductMark

def getProductMarks(request):
    marks=ProductMark.objects.all()
    return locals()