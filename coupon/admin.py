from .models import Coupon
from django.contrib import admin
class CouponsAdmin(admin.ModelAdmin):
	'''
		Admin View for Coupons
	'''
	list_display = ('code','valid_for','valid_to','discount','active',)
	list_filter = ('active','valid_for','valid_to',)
	search_fields = ('code',)

admin.site.register(Coupon, CouponsAdmin)
