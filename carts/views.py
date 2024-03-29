from django.db.models import query
from django.shortcuts import redirect, render, get_object_or_404

from products.models import Product

from .models import CartProducts
from .utils import get_or_create_cart

def cart(request):
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {
        'cart': cart
    })


def add(request):
    cart = get_or_create_cart(request)
    # product = Product.objects.get(pk=request.POST.get('product_id')) # Se puede utilizar ambos
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    # cart.products.add(product, through_defaults={
    #     'quantity': quantity
    # })

    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, 
                                                                product=product, 
                                                                quantity=quantity)

    return render(request, 'carts/add.html', {
        'quantity': quantity,
        'product': product
    })


def remove(request):
    cart = get_or_create_cart(request)
    # product = Product.objects.get(pk=request.POST.get('product_id'))
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')
