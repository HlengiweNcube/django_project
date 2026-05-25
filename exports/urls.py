from django.urls import path

from .views import (
    export_list,
    add_export
)

urlpatterns = [

    path(
        'exports/',
        export_list,
        name='export_list'
    ),

    path(
        'exports/add/',
        add_export,
        name='add_export'
    ),
]