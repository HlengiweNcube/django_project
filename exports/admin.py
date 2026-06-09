from django.contrib import admin
from .models import ExportRecord


@admin.register(ExportRecord)
class ExportRecordAdmin(admin.ModelAdmin):
	list_display = ('product', 'customer_name', 'quantity_exported', 'subtotal_amount', 'tax_amount', 'total_amount', 'export_date', 'created_at')
	search_fields = ('product__name', 'customer_name')
	list_filter = ('export_date',)
