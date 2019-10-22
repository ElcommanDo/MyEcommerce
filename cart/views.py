from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST

from coupon.forms import CouponApplyForm
from shop.models import Product
from .cart import cart
from .forms import CartAddProduct as CartAddProductForm

# Create your views here.
@require_POST
def add_to_cart(request,product_id):
     Cart = cart(request)
     product = Product.objects.get(id = product_id)
     form = CartAddProductForm(request.POST)
     if form.is_valid():
         cd = form.cleaned_data
         Cart.add_to_cart(
             product,
             cd['quantity'],
             cd['update']
         )
     return redirect('cart_details')
def delete_from_cart(request,product_id):
    Cart = cart(request)
    product = get_object_or_404(Product,id=product_id)
    Cart.remove(product)
    return redirect('cart_details')
def cart_details(request):
    Cart = cart(request)

    for item in Cart:
      item['update_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'],'update':True})
    coupon_apply_form = CouponApplyForm()


    context = {
		'cart':Cart,'coupon_apply_form':coupon_apply_form

    }
    return render(request,'cart/cart_details.html',context)





