from django.db import models 
from datetime import datetime


class Product(models.Model):
    x =[
        ('phone','phone'),
        ('computer','computer'),
        ('handphone','handphone')
    ]
    name = models.CharField(max_length=100,default='product')
    content = models.TextField(default='nun',null=True,blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,default=000)
    image = models.ImageField(upload_to= 'photos/%y/%m/%d',default='photos/23/11/17/AMP06914.JPG')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50,null=True,blank=True,choices=x)
    def __str__ (self):
        return self.name
    
   # class Meta :
     #   verbose_name='name'
      #  ordering = ['-price']

class Test (models.Model) :
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default= datetime)





     















    