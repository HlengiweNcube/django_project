from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required, permission_required

from .models import ExportRecord
from .forms import ExportRecordForm


@login_required
def export_list(request):

    exports = ExportRecord.objects.all()

    return render(
        request,
        'exports/export_list.html',
        {'exports': exports}
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

            return redirect('export_list')

    else:

        form = ExportRecordForm()

    return render(
        request,
        'exports/add_export.html',
        {'form': form}
    )