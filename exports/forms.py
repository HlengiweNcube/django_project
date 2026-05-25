from django import forms

from .models import ExportRecord


class ExportRecordForm(forms.ModelForm):

    class Meta:

        model = ExportRecord

        fields = [
            'product',
            'customer_name',
            'quantity_exported',
            'export_date',
            'notes',
        ]

        widgets = {

            'export_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

        }