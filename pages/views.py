from django.shortcuts import render

def index(request ):
    return render(request, 'pages/index.html')

  
def about(request ):
     Len = int(request.POST.get('username'))
     cou = int(request.POST.get('password')) 
     total = 2*3.14*(Len/2)
     test = (total*cou)/100
     return render(request,'pages/about.html',{'name':test})





   
