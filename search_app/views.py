from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        myquery = query.lower()
        # products = Products.raw('SELECT * FROM ')
        products = Product.objects.all().filter(Q(name__contains=myquery) | Q(description__contains=query))
        print (products,query)
    return render(request,'search.html',{'query':query,'products':products})
