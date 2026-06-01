from django.urls import path
from .views import (
    add_project,
    delete_product,
    product_list,
    add_product,
    update_product,
    project_list,
    update_project,
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
    path('projects/', project_list, name='project_list'),
    path('projects/add/', add_project, name='add_project_item'),
    path(
        'projects/update/<int:project_id>/',
        update_project,
        name='update_project'
    ),
]