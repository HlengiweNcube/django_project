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