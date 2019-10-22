from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from decimal import Decimal
from coupon.models import Coupon
from shop.models import Product
# Create your models here.

class Order(models.Model):
    f_name = models.CharField(max_length=120,verbose_name='first name')
    l_name = models.CharField(max_length=120,verbose_name='last name')
    email = models.EmailField(verbose_name='Email')
    post_code = models.CharField(max_length=20,verbose_name='post code')
    city = models.CharField(max_length=100,verbose_name='city')
    address = models.CharField(max_length=100,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    coupon 	= models.ForeignKey(Coupon,related_name='orders',on_delete=models.CASCADE ,null=True,blank=True)
    discount = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])


    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ('-created',)
    def __str__(self):
        return "{} order ".format(self.f_name)
    def get_total_cost(self):
        total_cost=sum(item.get_cost() for item in self.items.all())

        return total_cost - total_cost*(self.discount/Decimal('100'))
class OrderItem(models.Model):
	order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
	product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	quantity= models.PositiveIntegerField(default=1)

	class Meta:
		verbose_name = "OrderItem"
		verbose_name_plural = "OrderItems"


	def __str__(self):
		return '{}'.format(self.id)


	def get_cost(self):
		return self.price * self.quantity


