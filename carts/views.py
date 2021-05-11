from django.shortcuts import render

from .models import Cart

def cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')

    if cart_id:
        cart = Cart.objects.get(cart_id=cart_id)
    else:
        cart = Cart.objects.create(user=user)

    request.session['cart_id'] = cart.cart_id

    return render(request, 'carts/cart.html', {
        
    })
