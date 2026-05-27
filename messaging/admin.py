from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ('subject', 'sender', 'receiver', 'is_archived', 'created_at')
	search_fields = ('subject', 'sender__username', 'receiver__username')
	list_filter = ('is_archived', 'created_at')
