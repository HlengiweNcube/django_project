from django.urls import path
from .views import (
    delete_product,
    product_list,
    add_product,
    update_product
)

urlpatterns = [
    path('products/', product_list, name='product_list'),

    path('products/add/', add_product, name='add_product'),

     path(
        'products/update/<int:product_id>/',
        update_product,
        name='update_product'
    ),

    path(
        'products/delete/<int:product_id>/',
        delete_product,
        name='delete_product'
    ),
]