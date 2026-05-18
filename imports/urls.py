from django.urls import path

from .views import (
    import_list,
    add_import
)

urlpatterns = [

    path(
        'imports/',
        import_list,
        name='import_list'
    ),

    path(
        'imports/add/',
        add_import,
        name='add_import'
    ),
]