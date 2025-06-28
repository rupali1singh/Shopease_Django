from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from the products app!")


def product_list(request):
    products = Product.objects.all()
    return render(request, 'Template/products/product_list.html', {'products': products})