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

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        quantity_exported = cleaned_data.get('quantity_exported')

        if product and quantity_exported and quantity_exported > product.quantity:
            self.add_error(
                'quantity_exported',
                'Cannot export more than current stock quantity.'
            )

        return cleaned_data