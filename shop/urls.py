from django.urls import path
from .views import *
urlpatterns = [
   path('',product_list,name='product_list'),
   path('product_list_category/<slug:category_slug>/',product_list,name='product_list_category'),

   path('product_details/<int:id>/<slug:slug>/',product_details,name='product_details'),

]
