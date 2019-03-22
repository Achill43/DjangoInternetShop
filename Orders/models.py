from django.db import models
from Products.models import Product
from django.db.models.signals import post_save

# Create your models here.
class Status(models.Model):
    name=models.CharField(max_length=20)
    class Meta:
        verbose_name='Статус заказа'
        verbose_name_plural='Статусы заказа'

class Order(models.Model):
    customerName=models.CharField(max_length=100)
    customerEmail=models.EmailField()
    customerPhone=models.CharField(max_length=14, blank=True, null=True, default=None)
    comment=models.TextField()
    status=models.ForeignKey(Status, on_delete=models.PROTECT)
    allSume=models.IntegerField( blank=True, null=True, default=0)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return "%s | %s" % ( self.customerName, self.created)

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'

class ProductInOrder(models.Model):
    order=models.ForeignKey(Order, on_delete=models.PROTECT, blank=True, null=True, default=None)
    product=models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True, default=None)
    countProd=models.IntegerField()
    priceProduct=models.IntegerField(blank=True, null=True, default=0)
    totalPrice=models.IntegerField(blank=True, null=True, default=0)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
        
    def __str__(self):
        return "%s" % (  self.product.name)

    def save(self, *args, **kwargs):
        self.priceProduct=self.product.price
        self.totalPrice=self.product.price*self.countProd
        super(ProductInOrder, self).save(*args, *kwargs)
    
    class Meta:
        verbose_name='Товар в заказе'
        verbose_name_plural='Товары в заказе'

class ProductInCart(models.Model):
    sessionKey=models.CharField(max_length=255)
    order=models.ForeignKey(Order, on_delete=models.PROTECT, blank=True, null=True, default=None)
    product=models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True, default=None)
    countProd=models.IntegerField()
    priceProduct=models.IntegerField(blank=True, null=True, default=0)
    totalPrice=models.IntegerField(blank=True, null=True, default=0)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
        
    def __str__(self):
        return "%s" % (  self.product.name)

    def save(self, *args, **kwargs):
        self.priceProduct=self.product.price
        priceProduct=self.product.price
        self.totalPrice=int(self.countProd)*priceProduct
        super(ProductInCart, self).save(*args, *kwargs)
    
    class Meta:
        verbose_name='Товар в корзине'
        verbose_name_plural='Товары в корзине'

def myProductInOrderPostSave(sender, instance, created, **kwargs):
    order=instance.order
    allProducts=ProductInOrder.objects.filter(order=order)
    orderAllSume=55
    for item in allProducts:
        orderAllSume+=item.totalPrice

    instance.order.allSume=orderAllSume
    instance.order.save(update_fields=["allSume"])
    #Увага! В функції post_save не можна викликати save() для тої моделі яка відстежується в даному випадку ProductInOrder
    # Інакше винекне вічний цикл

post_save.connect(myProductInOrderPostSave, sender=ProductInOrder)
