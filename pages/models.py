from django.db import models
# علاقة الجداول
#علاقة واحد ل واحد

#علاقة كثير لكثير

class Female (models.Model):
    name_female = models.CharField (max_length=50 ,null=True)
    def __str__(self):
        return self.name_female
    
class Male (models.Model):
    name_male = models.CharField (max_length=50 ,null=True)
    girls = models.OneToOneField (Female ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name_male
    
#علاقة واحد لكثير
class Product (models.Model):
    name = models.CharField (max_length=50 ,null=True)
   

    def __str__(self):
        return self.name
class User (models.Model):
    name = models.CharField (max_length=50 ,null=True)
    products = models.ForeignKey (Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    # علاقة كثير لكثير
class Video (models.Model):
    name = models.CharField (max_length=50 ,null=True)
    def __str__(self):
        return self.name
    
class UserName (models.Model):
    name = models.CharField (max_length=50 ,null=True)
    watch = models.ManyToManyField (Video,null=True)
    def __str__(self):
        return self.name
    
class Login (models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
