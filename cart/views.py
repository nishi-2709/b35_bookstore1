from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from books.models import Book
from .models import Cart, CartItem
from django.http import JsonResponse

class CartView(View):
    def get(self, request):
        cart = self._get_cart(request)
        return render(request, 'cart/cart_detail.html', {'cart': cart})

    def _get_cart(self, request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            cart_id = request.session.get('cart_id')
            if cart_id:
                cart = get_object_or_404(Cart, id=cart_id)
            else:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
        return cart

class AddToCartView(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        cart = CartView()._get_cart(request)
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={'quantity': 1}
        )
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        messages.success(request, f'{book.title} added to cart!')
        return redirect('cart:cart-detail')

class RemoveFromCartView(View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart = cart_item.cart
        
        if request.user.is_authenticated and cart.user != request.user:
            messages.error(request, 'You do not have permission to modify this cart.')
            return redirect('cart:cart-detail')
        
        cart_item.delete()
        messages.success(request, 'Item removed from cart.')
        return redirect('cart:cart-detail')

class UpdateCartView(View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart = cart_item.cart
        
        if request.user.is_authenticated and cart.user != request.user:
            return JsonResponse({'error': 'Permission denied'}, status=403)
        
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            return JsonResponse({
                'success': True,
                'total_price': cart_item.get_total_price()
            })
        else:
            cart_item.delete()
            return JsonResponse({'success': True, 'removed': True}) 