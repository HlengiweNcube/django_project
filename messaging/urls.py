from django.urls import path

from .views import (
    inbox,
    send_message,
    archive_message
)

urlpatterns = [

    path(
        'messages/',
        inbox,
        name='inbox'
    ),

    path(
        'messages/send/',
        send_message,
        name='send_message'
    ),

    path(
        'messages/archive/<int:message_id>/',
        archive_message,
        name='archive_message'
    ),
]