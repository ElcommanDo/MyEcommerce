from django.contrib import admin
from .models import OrderItem,Order
from django.urls import reverse
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportActionModelAdmin
def order_pdf(obj):
	return mark_safe('<a href="{}">PDF</a>'.format(reverse('admin_order_pdf',args=[obj.id])))
class OrderItemAdmin(admin.TabularInline):
	'''
		Admin View for OrderItem
	'''
	model = OrderItem
	raw_id_fields = ['product']

class OrderAdmin(ImportExportActionModelAdmin):
	'''
		Admin View for Order
	'''
	list_display = ('id','f_name','l_name','address','email','city','post_code','paid',order_pdf,)
	list_filter = ('paid','created','updated',)
	search_fields = ['f_name','l_name','email']
	inlines = [
	OrderItemAdmin,
	]

admin.site.register(Order, OrderAdmin)
