from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .forms import OrderCreateForm
from .models import OrderItem,Order
from cart.cart import cart
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
#import weasyprint
@staff_member_required
def admin_order_pdf(request,order_id):

	order = get_object_or_404(Order,id=order_id)
	html = render_to_string('order/pdf.html',{'order':order})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)
	#weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])

	return response


def create_order(request):
    Cart = cart(request)
    if request.method == 'POST':
      form = OrderCreateForm(request.POST)
      if form.is_valid():
        order = form.save(commit=False)
        if Cart.coupon:
            order.coupon = Cart.coupon
            order.discount = Cart.coupon.discount
        order.save()


      for item in Cart:
          OrderItem.objects.create(order=order,
                                   product=item['product'],
                                   price=item['price'],
                                   quantity=item['quantity']
          )
      Cart.clear()
      context = { 'order' :order}
      request.session['order_id'] = order.id
      return redirect(reverse('payment:process'))
      #return render(request,'order/thanks.html',context)
    else:
        form = OrderCreateForm()
    context = {'form':form,'cart':Cart}
    return render(request,'order/create.html',context)



