from django.shortcuts import render

# Create your views here.
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from the cart app!")

