from django import forms
from .models import Product, Project


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'name',
            'category',
            'quantity',
            'price',
            'description',
        ]
        labels = {
            'name': 'Product name',
            'category': 'Category',
            'quantity': 'Quantity in stock',
            'price': 'Unit price',
            'description': 'Product description',
        }
        help_texts = {
            'category': 'Choose the category that best matches the product.',
            'quantity': 'Enter the number of items currently available.',
            'price': 'Enter the price per item.',
        }
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'quantity': forms.NumberInput(attrs={'min': 0, 'inputmode': 'numeric'}),
            'price': forms.NumberInput(attrs={'min': 0, 'step': '0.01', 'inputmode': 'decimal'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'start_date',
            'end_date',
            'stakeholders',
            'status',
            'category',
        ]
        labels = {
            'name': 'Project name',
            'description': 'Project description',
            'start_date': 'Start date',
            'end_date': 'End date',
            'stakeholders': 'Stakeholders',
            'status': 'Status',
            'category': 'Category',
        }
        help_texts = {
            'stakeholders': 'List names separated by commas.',
            'status': 'Select the current stage of the project.',
            'category': 'Choose the category that best matches the project.',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'stakeholders': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date < start_date:
            self.add_error('end_date', 'End date cannot be before start date.')

        return cleaned_data