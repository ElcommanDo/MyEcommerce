from django.urls import path
from . import views

urlpatterns = [
	path('create/',views.create_order,name='create_order'),
	path(r'^admin/order/(?P<order_id>\d+)/pdf/$', views.admin_order_pdf, name='admin_order_pdf'),
]
