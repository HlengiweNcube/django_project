from django.contrib import admin
from .models import Product, Project


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'quantity', 'price', 'created_at')
	search_fields = ('name', 'category')
	list_filter = ('category',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'status', 'category', 'start_date', 'end_date')
	search_fields = ('name', 'owner__username', 'stakeholders')
	list_filter = ('status', 'category')
