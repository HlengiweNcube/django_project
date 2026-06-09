from django.contrib import admin
from .models import ImportRecord


@admin.register(ImportRecord)
class ImportRecordAdmin(admin.ModelAdmin):
	list_display = ('product', 'supplier_name', 'quantity_imported', 'subtotal_amount', 'tax_amount', 'total_amount', 'import_date', 'created_at')
	search_fields = ('product__name', 'supplier_name')
	list_filter = ('import_date',)
