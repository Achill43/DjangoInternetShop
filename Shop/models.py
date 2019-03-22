from django.db import models

class Subscribers(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=14)
    def __str__(self):
        return "%s | %s | %s" % (self.email, self.name, self.phone)

    class Meta:
        verbose_name='Subscriber'
        verbose_name_plural='Subscribers'
