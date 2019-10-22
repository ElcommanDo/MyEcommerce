from django.urls import path
from .views import *
urlpatterns = [
  path('cart_add/<int:product_id>',add_to_cart,name='cart_add'),
  path('cart_remove/<int:product_id>',delete_from_cart,name='cart_remove'),
  path('cart_details',cart_details,name = 'cart_details'),

]
