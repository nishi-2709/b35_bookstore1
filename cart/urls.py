from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart-detail'),
    path('add/<int:book_id>/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('remove/<int:item_id>/', views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('update/<int:item_id>/', views.UpdateCartView.as_view(), name='update-cart'),
] 