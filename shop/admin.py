from django.contrib import admin
from .models import Category,Product
from django.utils.safestring import mark_safe

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	'''
		Admin View for Category
	'''
	list_display = ('name','slug',)
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):

	'''
		Admin View for Product
	'''
	@mark_safe
	def preview(self,obj):

   		return '<img src="{}" width=100/>'.format(obj.Image.url)
	preview.allow_tags = True
	list_display = ('preview','name','slug','category','price','stock','available','created','updated',)
	list_filter = ('available','created','updated','category',)
	list_editable = ('price','stock','available',)
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Product, ProductAdmin)
