from django.db import models

# Create your models here.
class ProductMark(models.Model):
    name=models.CharField(max_length=55)
    isActive=models.BooleanField(default=True)

    def __str__(self):
        return "%s"%(self.name)

    class Meta:
        verbose_name='Марка'
        verbose_name_plural='Марки'

class Product(models.Model):
    name=models.CharField(max_length=55)
    publish=models.BooleanField(default=True)
    mark=models.ForeignKey(ProductMark, on_delete=models.PROTECT)
    news=models.BooleanField(default=True)
    hits=models.BooleanField(default=False)
    sale=models.BooleanField(default=False)
    isActive=models.BooleanField(default=True)
    mainImg=models.ImageField(upload_to='static/Shop/img/goods/')
    price=models.IntegerField()
    descriction=models.TextField()
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s | %s грн" % (self.name, self.price)

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

class ImageForProduct(models.Model):
    product=models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True, default=None)
    img=models.ImageField(upload_to='static/Shop/img/goods/')
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "%s" % (self.product.name)
    class Meta:
        verbose_name='Картинка для товара'
        verbose_name_plural='Картинки для товара'
