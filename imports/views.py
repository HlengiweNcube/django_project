from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import ImportRecord
from .forms import ImportRecordForm


@login_required
def import_list(request):

    imports = ImportRecord.objects.all()

    return render(
        request,
        'imports/import_list.html',
        {'imports': imports}
    )


@login_required
def add_import(request):

    if request.method == 'POST':

        form = ImportRecordForm(request.POST)

        if form.is_valid():

            import_record = form.save()

            product = import_record.product

            product.quantity += import_record.quantity_imported

            product.save()

            return redirect('import_list')

    else:

        form = ImportRecordForm()

    return render(
        request,
        'imports/add_import.html',
        {'form': form}
    )