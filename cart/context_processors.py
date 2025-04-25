from .models import Cart, CartItem

def cart(request):
    cart = None
    cart_items = []
    total_items = 0
    total_price = 0

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.filter(id=cart_id).first()

    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
        total_items = sum(item.quantity for item in cart_items)
        total_price = sum(item.get_total_price() for item in cart_items)

    return {
        'cart': cart,
        'cart_items': cart_items,
        'total_items': total_items,
        'total_price': total_price,
    } 