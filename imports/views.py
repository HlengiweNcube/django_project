from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import ImportRecord
from .forms import ImportRecordForm
from inventory.models import Product


@login_required
def import_list(request):

    imports = ImportRecord.objects.all()

    return render(
        request,
        'imports/import_list.html',
        {'imports': imports}
    )


@login_required
@permission_required('imports.add_importrecord', raise_exception=True)
def add_import(request):

    if request.method == 'POST':

        form = ImportRecordForm(request.POST)

        if form.is_valid():

            import_record = form.save()

            product = import_record.product

            product.quantity += import_record.quantity_imported

            product.save()
            messages.success(request, 'Import recorded and stock updated.')

            return redirect('import_list')

    else:

        form = ImportRecordForm()

    has_products = Product.objects.exists()

    return render(
        request,
        'imports/add_import.html',
        {
            'form': form,
            'has_products': has_products,
        }
    )
