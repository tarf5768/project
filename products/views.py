from django.shortcuts import render
from .models import Product 

  
def product(request ):
     return render(request, 'products/product.html')

  
def products(request ): 
      # y= {'pro':Product.objects.get(id=1)}   لمنتج واحد
     tes = Product.objects.all()
     # x = {'pro':pro.filter(category='phone')} # فلترة
     # x = {'pro':pro.filter(category__exact='phone')}  # فلتر اختيار نوع
     # x = {'pro':tes.filter(category__contains='com')}  # بحث باي احرف من النوع
     # x = {'pro':tes.filter(price__in=[100,59])}   # بحث عن اكثر من واحدة
     x = {'pro':tes.filter(price__range=(0,9999))}     # البحث عن رينج بين قيمتين
      # x={'pro':te.exclude(price=0) } # وعرض الجميع باستثناء نوع 
      # x = {'pro':str(pro.count())}  # عدد المنتجات 
     return render(request, 'products/products.html', x)


