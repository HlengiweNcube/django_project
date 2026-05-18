from django import forms

from .models import ImportRecord


class ImportRecordForm(forms.ModelForm):

    class Meta:

        model = ImportRecord

        fields = [
            'product',
            'supplier_name',
            'quantity_imported',
            'import_date',
            'notes',
        ]

        widgets = {

            'import_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

        }