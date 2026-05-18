from django.urls import path
from .views import (
    product_list,
    add_product
)

urlpatterns = [
    path('products/', product_list, name='product_list'),

    path('products/add/', add_product, name='add_product'),
]