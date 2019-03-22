from django.db import models

# Create your models here.

class Customer(models.Model):
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=16)
    name=models.CharField(max_length=150)
    dateOfBirthday=models.DateField()
    def __str__(self):
        return "%s | %s" % (self.email, self.name)

    class Meta:
        verbose_name='Покупатель'
        verbose_name_plural='Покупатели'