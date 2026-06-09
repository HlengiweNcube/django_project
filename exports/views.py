from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from inventory.models import Product

from .models import ExportRecord
from .forms import ExportRecordForm


@login_required
def export_list(request):

    exports = ExportRecord.objects.all()
    default_tax_rate_percent = Decimal(str(getattr(settings, 'DEFAULT_TAX_RATE', '0.15'))) * Decimal('100')

    return render(
        request,
        'exports/export_list.html',
        {
            'exports': exports,
            'default_tax_rate_percent': default_tax_rate_percent,
        }
    )


@login_required
@permission_required('exports.add_exportrecord', raise_exception=True)
def add_export(request):

    if request.method == 'POST':

        form = ExportRecordForm(request.POST)

        if form.is_valid():

            export_record = form.save()

            product = export_record.product

            product.quantity -= export_record.quantity_exported

            product.save()
            messages.success(request, 'Export recorded and stock updated.')

            return redirect('export_list')

    else:

        form = ExportRecordForm()

    has_products = Product.objects.exists()
    default_tax_rate_percent = Decimal(str(getattr(settings, 'DEFAULT_TAX_RATE', '0.15'))) * Decimal('100')

    return render(
        request,
        'exports/add_export.html',
        {
            'form': form,
            'has_products': has_products,
            'default_tax_rate_percent': default_tax_rate_percent,
        }
    )