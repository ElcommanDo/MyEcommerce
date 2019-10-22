from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)
    valid_to = models.DateTimeField()
    valid_for = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField()
    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"
    def __str__(self):
        return self.code



