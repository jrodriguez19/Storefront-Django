from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.


def sayHello(request):
    querySet = Product.objects.all()

    # querysets are only evaluated when called like in the following for loop
    for product in querySet:
        print(product)

    return render(request, "hello.html", {'name': 'Georgito!'})
