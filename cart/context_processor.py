from .cart import cart
def Cart(request):
    return {'cart': cart(request)}
